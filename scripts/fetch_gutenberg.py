#!/usr/bin/env python3
"""Fetch the verified Project Gutenberg public-domain candidates into books/.

This script downloads only the explicitly listed texts. Review local copyright
rules before redistribution. Project Gutenberg notes that readers outside the
United States must check their own country's laws.
"""
from __future__ import annotations

import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOKS = ROOT / "books" / "en"
METADATA = ROOT / "metadata"
USER_AGENT = "shudan-personal-library/1.0 (public-domain text fetcher)"

SOURCES = [
    {
        "id": "pg-445",
        "title": "The Crowd: A Study of the Popular Mind",
        "author": "Gustave Le Bon",
        "year": 1896,
        "language": "en",
        "url": "https://www.gutenberg.org/cache/epub/445/pg445.txt",
        "catalog_url": "https://www.gutenberg.org/ebooks/445",
        "filename": "the-crowd-gustave-le-bon.txt",
    },
    {
        "id": "pg-833",
        "title": "The Theory of the Leisure Class",
        "author": "Thorstein Veblen",
        "year": 1899,
        "language": "en",
        "url": "https://www.gutenberg.org/cache/epub/833/pg833.txt",
        "catalog_url": "https://www.gutenberg.org/ebooks/833",
        "filename": "the-theory-of-the-leisure-class-thorstein-veblen.txt",
    },
    {
        "id": "pg-1227",
        "title": "The Expression of the Emotions in Man and Animals",
        "author": "Charles Darwin",
        "year": 1899,
        "language": "en",
        "url": "https://www.gutenberg.org/cache/epub/1227/pg1227.txt",
        "catalog_url": "https://www.gutenberg.org/ebooks/1227",
        "filename": "the-expression-of-the-emotions-charles-darwin.txt",
    },
    {
        "id": "pg-6456",
        "title": "Public Opinion",
        "author": "Walter Lippmann",
        "year": 1922,
        "language": "en",
        "url": "https://www.gutenberg.org/cache/epub/6456/pg6456.txt",
        "catalog_url": "https://www.gutenberg.org/ebooks/6456",
        "filename": "public-opinion-walter-lippmann.txt",
    },
    {
        "id": "pg-37134",
        "title": "The Elements of Style",
        "author": "William Strunk Jr.",
        "year": 1918,
        "language": "en",
        "edition_note": "Original Strunk text; not the later Strunk & White expansion.",
        "url": "https://www.gutenberg.org/cache/epub/37134/pg37134.txt",
        "catalog_url": "https://www.gutenberg.org/ebooks/37134",
        "filename": "the-elements-of-style-william-strunk.txt",
    },
]


def fetch(source: dict) -> dict:
    request = urllib.request.Request(
        source["url"],
        headers={"User-Agent": USER_AGENT},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        if response.status != 200:
            raise RuntimeError(f"{source['id']}: HTTP {response.status}")
        raw = response.read()
    text = raw.decode("utf-8-sig")
    if len(text) < 10_000 or "Project Gutenberg" not in text[:2_000]:
        raise RuntimeError(f"{source['id']}: response does not look like a Gutenberg text")
    target = BOOKS / source["filename"]
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    return {
        **source,
        "local_path": str(target.relative_to(ROOT)),
        "bytes": len(raw),
        "status": "downloaded",
        "rights_note": (
            "Project Gutenberg lists this text as public domain in the USA. "
            "Check local law and the specific edition/translation before redistribution."
        ),
        "retrieved_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }


def main() -> None:
    METADATA.mkdir(parents=True, exist_ok=True)
    records = []
    errors = []
    for source in SOURCES:
        try:
            record = fetch(source)
            records.append(record)
            print(f"Downloaded: {source['title']} ({record['bytes']} bytes)")
        except Exception as exc:  # report each source and continue
            errors.append({"id": source["id"], "error": str(exc)})
            print(f"FAILED: {source['title']}: {exc}")
    (METADATA / "gutenberg-downloads.json").write_text(
        json.dumps({"books": records, "errors": errors}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    if errors:
        raise SystemExit(f"{len(errors)} source(s) failed; see metadata/gutenberg-downloads.json")


if __name__ == "__main__":
    main()
