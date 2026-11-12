"""
RECORD CHECK  -  my version
===========================

Name  :  Rushd Tariq
Lane  :  AI / Cyber / IT      (delete two)
Date  :  12/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """Clean and parse one messy security record."""

    clean_line = raw_line.strip().lower()

    data = {}

    for piece in clean_line.split(","):
        key, value = piece.split("=")

        key = key.strip()
        value = value.strip()

        if key == "attempts":
            data[key] = int(value)
        else:
            data[key] = value

    return data


def status_of(record):
    """Check whether a login record needs security attention."""

    if record["result"] == "failed" or record["attempts"] >= 10:
        return "FLAGGED"
    else:
        return "OK"


# ====================================================================== INPUT

raw_records = [
    "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED",
    "  src=10.0.0.8 , attempts=3 , result=success  ",
    "SRC = 192.168.1.10 , ATTEMPTS = 15 , RESULT = failed",
    "  Src=172.16.0.4, attempts=2, RESULT=SUCCESS ",
    "src=10.0.0.20 , ATTEMPTS=8 , result=FAILED"
]


# =============================================================== PROCESS + OUTPUT

total_records = 0
flagged_records = 0

for raw_record in raw_records:

    try:
        record = parse_line(raw_record)

        status = status_of(record)

        print(record, status)

        total_records += 1

        if status == "FLAGGED":
            flagged_records += 1

    except (ValueError, KeyError):
        print("Could not parse:", raw_record)

print("\n--- SECURITY SUMMARY ---")
print("Total records:", total_records)
print("Flagged records:", flagged_records)
