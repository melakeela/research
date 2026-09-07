#!/usr/bin/env python3
"""
csvdialect.py — read and rewrite this repository's CSVs without reformatting them.

The registers were written by different scripts and different sessions. They
mix CRLF and LF line endings and they mix QUOTE_ALL against QUOTE_MINIMAL.
A migration that normalises either one produces a diff in which every row
looks changed, which destroys review. Everything here sniffs what a file
already does and writes it back the same way.
"""
import csv
import io


def sniff(path):
    """Return (quoting, lineterminator) as the file on disk already uses them."""
    with open(path, "rb") as fh:
        head = fh.read(65536)
    lineterminator = "\r\n" if b"\r\n" in head else "\n"
    # QUOTE_ALL writers quote the header; minimal writers only quote when forced,
    # and no header field in this repository contains a comma or a quote.
    quoting = csv.QUOTE_ALL if head[:1] == b'"' else csv.QUOTE_MINIMAL
    return quoting, lineterminator


def read(path):
    """Return (fieldnames, rows) with rows as dicts. Never mutates the file."""
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        return list(reader.fieldnames or []), rows


def write(path, fieldnames, rows, quoting=None, lineterminator=None):
    """Write rows back in the file's own dialect, or in one given explicitly."""
    if quoting is None or lineterminator is None:
        sq, sl = sniff(path)
        quoting = sq if quoting is None else quoting
        lineterminator = sl if lineterminator is None else lineterminator
    buf = io.StringIO(newline="")
    writer = csv.DictWriter(
        buf, fieldnames=fieldnames, quoting=quoting,
        lineterminator=lineterminator, extrasaction="ignore",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow({k: (row.get(k) or "") for k in fieldnames})
    with open(path, "w", newline="", encoding="utf-8") as fh:
        fh.write(buf.getvalue())
