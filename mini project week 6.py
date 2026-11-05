"""
RECORD CHECK - my version
===========================

Name  : Rushd Tariq
Lane  : Cyber Security
Date  : 05/11/2026

Run it: python template.py
"""

import pandas as pd
import matplotlib.pyplot as plt

with open("records_sample.csv", "w") as file:
    file.write("source_ip,failed_logins,total_attempts\n")
    file.write("10.0.0.5,100,100\n")
    file.write("10.0.0.8,95,100\n")
    file.write("10.0.0.12,12,400\n")
    file.write("10.0.0.15,93,100\n")
    file.write("10.0.0.20,45,100\n")
    file.write("10.0.0.25,67,100\n")

print("CSV file created successfully!")
# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: source_ip,failed_logins,total_attempts.

df = pd.read_csv("records_sample.csv")


# ================================================================= PROCESS
# 2. Add a "percent" column: (failed_logins / total_attempts) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

df["percent"] = (df["failed_logins"] / df["total_attempts"]) * 100

df["status"] = df["percent"].apply(lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK"))


# ================================================================== OUTPUT
# 3. Print the DataFrame.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

print(df)

# Show only rows that are not OK
print(df[df["status"] != "OK"])

# Group by status and print a count per group
print(df.groupby("status").size())

# Save the full DataFrame to a new CSV
df.to_csv("cyber_report.csv", index=False)

# Create and save a bar chart of the counts per status
df["status"].value_counts().plot(kind="bar")

plt.title("Cyber Security Status Counts")
plt.xlabel("Status")
plt.ylabel("Count")

plt.savefig("status_counts.png")
plt.show()


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case