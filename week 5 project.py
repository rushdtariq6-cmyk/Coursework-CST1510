"""
RECORD CHECK  -  my version
===========================

Name  :  Rushd Tariq
Lane  :  AI / Cyber / IT      (delete two)
Date  :  22/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



class Record:
    over_limit_count = 0
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def summary(self):
        return (self.value / self.limit) * 100

    def status(self):
        percentage = self.percent()
        
        if percentage >= 100:
            Record.over_limit_count +=1
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"


records = [ 
Record("R-001", 87.0, 100.0)
Record("R-002", 120.0, 100.0)
]



for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print("Label:", record.label)
    print("Value:", record.value)
    print("limit:", record.limit)
    print("status:", record.status())

    print("=" * 34)


