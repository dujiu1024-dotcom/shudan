#!/usr/bin/env python3
"""Fetch documented open-access book PDFs from Internet Archive mirrors.

Rights are checked against the cited official item records before adding entries
to this fixed allowlist. The PDF bytes are validated before being saved.
"""
from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "books" / "pdf"
META = ROOT / "metadata"
UA = "shudan-personal-library/1.0 (open-access book collector)"

SOURCES = [
    {
        "id": "ia-free-culture",
        "title": "Free Culture: How Big Media Uses Technology and the Law to Lock Down Culture and Control Creativity",
        "author": "Lawrence Lessig",
        "archive_identifier": "free_culture",
        "preferred_filename": "freeculture.pdf",
        "filename": "free-culture-lawrence-lessig.pdf",
        "rights_source": "https://lessig.org/product/free-culture/",
        "rights_basis": "The author’s official page states that the PDF version may be copied and redistributed for non-commercial purposes with attribution; the PDF itself states CC BY-NC 1.0.",
        "catalog_id": "BK188",
    },
    {
        "id": "ia-aristotle-rhetoric",
        "title": "Aristotle's Treatise on Rhetoric",
        "author": "Aristotle; Thomas Hobbes; Theodore Alois Buckley",
        "archive_identifier": "aristotlestreati00aris_0",
        "preferred_filename": "aristotlestreati00aris_0.pdf",
        "filename": "aristotles-treatise-on-rhetoric-1872.pdf",
        "rights_source": "https://www.loc.gov/item/17028328/",
        "rights_basis": "Library of Congress identifies the 1872 edition as public domain and free to use and reuse. Candidate match only because the user's list gives no author or edition.",
        "catalog_id": "BK042",
    },
]


def archive_pdf_url(source):
    metadata_url = "https://archive.org/metadata/" + source["archive_identifier"]
    req = urllib.request.Request(metadata_url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as response:
        metadata = json.loads(response.read().decode("utf-8"))
    files = metadata.get("files", [])
    names = [f.get("name", "") for f in files if f.get("name", "").lower().endswith(".pdf")]
    preferred = source["preferred_filename"]
    chosen = preferred if preferred in names else None
    if not chosen:
        # Exclude OCR derivatives where a scanned source PDF exists.
        candidates = [n for n in names if not n.lower().endswith("_text.pdf")]
        if len(candidates) == 1:
            chosen = candidates[0]
        else:
            raise RuntimeError(f"{source['id']}: expected PDF not found; candidates={candidates[:10]}")
    return "https://archive.org/download/" + source["archive_identifier"] + "/" + urllib.parse.quote(chosen)


def fetch(source):
    pdf_url = archive_pdf_url(source)
    req = urllib.request.Request(pdf_url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as response:
        raw = response.read()
    if not raw.startswith(b"%PDF") or len(raw) < 20_000:
        raise RuntimeError(f"{source['id']}: response is not a valid-looking PDF")
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
        raise SystemExit(f"{len(errors)} open-book source(s) failed; see metadata/loc-downloads.json")


if __name__ == "__main__":
    main()
