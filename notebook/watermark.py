#!/usr/bin/env python3
"""Stamp buyer info into product files for delivery.

Usage:
  python3 watermark.py buyer@email.com ORDER123 [file1.html file2.html ...]

With no files listed, stamps all 7 shippable product files and writes the
output into a fresh folder named after the order ID, ready to zip and send.
"""
import sys
import datetime
import pathlib

PRODUCT_FILES = [
    "15-minute-quick-fix-checklist.html",
    "get-found-on-google-maps.html",
    "the-complete-google-maps-guide.html",
    "business-category-and-search-terms-guide.html",
    "no-tech-quick-start-guide.html",
    "ready-to-send-scripts.html",
    "local-listings-companion.html",
]

def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    email, order_id = sys.argv[1], sys.argv[2]
    files = sys.argv[3:] or PRODUCT_FILES
    today = datetime.date.today().isoformat()

    out_dir = pathlib.Path(f"delivery-{order_id}")
    out_dir.mkdir(exist_ok=True)

    for name in files:
        src = pathlib.Path(name)
        if not src.exists():
            print(f"skip (not found): {name}")
            continue
        text = src.read_text(encoding="utf-8")
        text = (text
                .replace("{{BUYER_EMAIL}}", email)
                .replace("{{ORDER_ID}}", order_id)
                .replace("{{PURCHASE_DATE}}", today))
        (out_dir / name).write_text(text, encoding="utf-8")
        print(f"stamped: {name}")

    print(f"\nDone. Deliver the files in ./{out_dir}/")

if __name__ == "__main__":
    main()
