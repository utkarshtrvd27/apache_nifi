#!/usr/bin/env python3
import csv
import json
import sys
import io
import traceback

def main():
    try:
        # Read stdin as text with UTF-8
        text_stream = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8", newline="")
        reader = csv.DictReader(text_stream)

        out_obj = {}
        for idx, row in enumerate(reader, start=1):
            out_obj[str(idx)] = row

        # Write a single JSON object (pretty printed)
        sys.stdout.write(json.dumps(out_obj, ensure_ascii=False, indent=2))
        sys.stdout.flush()
    except Exception:
        # Write a JSON error object to stdout so NiFi captures it in the FlowFile
        err = {"error": "csv_to_json_failed", "message": traceback.format_exc()}
        try:
            sys.stdout.write(json.dumps(err, ensure_ascii=False) + "\n")
            sys.stdout.flush()
        except Exception:
            sys.stderr.write("csv_to_json_failed\n")
        sys.exit(1)

if __name__ == "__main__":
    main()