# pybank python challenge
# GT Python Homework 07032021


# Time to begin, let's start with importing the OS and CSV file that we will use for this exercise analysis.
import os
import csv

# Point script (code) to a file to compare the data provided, create variable for file location.
csvpath =os.path.join(".","Resources", "budget_data.csv")

# create the list variable
budget = []

# Create a csv utilizing the file path and populate list
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
    budget.append(csv_header)
    for row in csvreader:
        budget.append(row)
        
# Set variables for finding net total and Month Count        
# Sount the rows starting from second row
# Sum all net totals together
Month_Count = 0
Net_Total = 0
for row in budget[1:]:
    Month_Count += 1
    Net_Total += int(row[1])
    
# Create a list of only the month totals
Month_Total = [int(j) for i, j in budget[1:]]

# Zip the month total list to itself & find difference between zipped items
Month_Change = [x - y for x, y in zip(Month_Total[1:], Month_Total)]

# Find the average of the items in the month change list
Month_Change_Avg = sum(Month_Change) / len(Month_Change)

# Create a list of the month names
Month_List = [i for i, j in budget[1:]]

# Zip the month names and month change list together
# Account for the first month not having a recorded change
Month_Change_List = [i for i in zip(Month_List[1:], Month_Change)]

for row in Month_Change_List:
    if row[1] == max(Month_Change):
        Max_Month = row[0]
        Max_Amount = row[1]
    if row[1] == min(Month_Change):
        Month_Min = row[0]
        Month_Amount = row[1]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(budget) - 1}")
print(f"Total: ${Net_Total}")
print(f"Average  Change: ${round(Month_Change_Avg, 2)}")
print(f"Greatest Increase in Profits: {Max_Month} (${max(Month_Change)})")
print(f"Greatest Decrease in Profits: {Month_Min} (${min(Month_Change)})")

with open("FinancialAnalysis.txt", "a") as txt:
    txt.write("Financial Analysis\n")
    txt.write("----------------------------\n")
    txt.write(f"Total Months: {len(budget) - 1}\n")
    txt.write(f"Total: ${Net_Total}\n")
    txt.write(f"Average  Change: ${round(Month_Change_Avg, 2)}\n")
    txt.write(f"Greatest Increase in Profits: {Max_Month} (${max(Month_Change)})\n")
    txt.write(f"Greatest Decrease in Profits: {Month_Min} (${min(Month_Change)})\n")
    txt.close()
