"""
RECORD CHECK  -  my version
===========================

Name  :  Rushd Tariq
Lane  :  AI / Cyber / IT      (delete two)
Date  :  15/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def check_record(value, limit):
    """Calculate the difference, percentage and status."""

    difference = value - limit
    percent = (value / limit) * 100 

    if value > limit:
        status = "OVER LIMIT"
    elif value == limit:
        status = "AT LIMIT"
    else:
        status = "WITHIN LIMIT"

    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    print(f"\nLabel: {label}")
    print(f"Value: {value}")
    print(f"Limit: {limit}")
    print(f"Difference: {difference}")
    print(f"Percentage: {percent:.2f}%")
    print(f"Status: {status}")

records = [{"label": "R-001", "value": 87.0, "limit": 100.0},
    {"label": "R-002", "value": 120.0, "limit": 100.0},
    {"label": "R-003", "value": 100.0, "limit": 100.0},
    {"label": "R-004", "value": 45.0, "limit": 50.0}
]
over_limit_count = 0

for record in records:
    difference, percent, status = check_record(record["value"],record["limit"])
    print_report(record["label"],record["value"],record["limit"],difference,percent,status)

    if status == "OVER LIMIT":
        over_limit_count += 1

