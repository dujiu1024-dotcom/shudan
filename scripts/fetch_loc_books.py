#!/usr/bin/env python3
"""Fetch open-access Library of Congress book PDFs after checking rights metadata."""
from __future__ import annotations

import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "books" / "pdf"
META = ROOT / "metadata"
UA = "shudan-personal-library/1.0 (open-access book collector)"

SOURCES = [
    {
        "id": "loc-2019666613",
        "title": "Free Culture: How Big Media Uses Technology and the Law to Lock Down Culture and Control Creativity",
        "author": "Lawrence Lessig",
        "item_url": "https://www.loc.gov/item/2019666613/",
        "rights_required": "CC BY 4.0",
        "rights_match": ["Creative Commons Attribution 4.0", "CC BY 4.0"],
        "filename": "free-culture-lawrence-lessig.pdf",
        "catalog_id": "BK188",
        "rights_note": "Library of Congress item record identifies CC BY 4.0; preserve attribution to Lawrence Lessig and cite the LOC record.",
    },
    {
        "id": "loc-17028328",
        "title": "Aristotle's Treatise on Rhetoric",
        "author": "Aristotle; Thomas Hobbes; Theodore Alois Buckley",
        "item_url": "https://www.loc.gov/item/17028328/",
        "rights_required": "Public domain",
        "rights_match": ["public domain", "free to use and reuse"],
        "filename": "aristotles-treatise-on-rhetoric-1872.pdf",
        "catalog_id": "BK042",
        "rights_note": "Library of Congress identifies this 1872 English edition as public domain. Candidate match only: the user's list says Rhetoric without author or edition.",
    },
]


def walk_strings(value):
    if isinstance(value, dict):
        for child in value.values():
            yield from walk_strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_strings(child)
    elif isinstance(value, str):
        yield value


def find_pdf_url(value):
    candidates = []
    for text in walk_strings(value):
        if text.startswith("https://") and ".pdf" in text.lower():
            candidates.append(text)
    # Prefer LOC's stable tile delivery host.
    candidates.sort(key=lambda u: (0 if "tile.loc.gov" in u else 1, len(u)))
    return candidates[0] if candidates else None


def fetch(source):
    api = source["item_url"] + "?fo=json"
    req = urllib.request.Request(api, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as response:
        payload = json.loads(response.read().decode("utf-8"))
    rights_blob = " ".join(walk_strings(payload)).lower()
    if not any(term.lower() in rights_blob for term in source["rights_match"]):
        raise RuntimeError(f"{source['id']}: required rights statement not found in item JSON")
    pdf_url = find_pdf_url(payload)
    if not pdf_url:
        raise RuntimeError(f"{source['id']}: no direct PDF URL found in LOC item JSON")
    req = urllib.request.Request(pdf_url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as response:
        raw = response.read()
    if not raw.startswith(b"%PDF") or len(raw) < 20_000:
        raise RuntimeError(f"{source['id']}: downloaded file is not a valid-looking PDF")
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / source["filename"]
    target.write_bytes(raw)
    return {
        **source,
        "pdf_url": pdf_url,
        "local_path": str(target.relative_to(ROOT)),
        "bytes": len(raw),
        "status": "downloaded",
        "retrieved_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }


def main():
    META.mkdir(parents=True, exist_ok=True)
    records, errors = [], []
    for source in SOURCES:
        try:
            item = fetch(source)
            records.append(item)
            print(f"Downloaded: {source['title']} ({item['bytes']} bytes)")
        except Exception as exc:
            errors.append({"id": source["id"], "error": str(exc)})
            print(f"FAILED: {source['title']}: {exc}")
    (META / "loc-downloads.json").write_text(
        json.dumps({"books": records, "errors": errors}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    if errors:
        raise SystemExit(f"{len(errors)} LOC source(s) failed; see metadata/loc-downloads.json")


if __name__ == "__main__":
    main()
