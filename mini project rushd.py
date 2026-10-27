"""
RECORD CHECK  -  my version
===========================

Name  :  Rushd Tariq
Lane  :  AI / Cyber / IT      (delete two)
Date  :  27/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

label = input("Enter label: ")            
value = float(input("Enter value: "))   
limit = float(input("Enter limit: "))    

difference = value - limit 
percent = (difference/limit) * 100       
   
if percent >= 100:
    status = "OVER LIMIT"

elif percent >= 90:
    status = "WARNING"  

else: 
    status = "OK"

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print("=" * 34)
