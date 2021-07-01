# pybank python challenge
# GT Python Homework
# pybank python challenge
# GT Python Homework 07032021


# import add ons:  Os Library & CSV Library
import os 
import csv


# Time to begin, let's start with importing the OS and CSV file that we will use for this exercise analysis.
import os
import csv

# The file location has to be determined by a variable
# Point script (code) to a file to compare the data provided
# Set the file location as a variable 
csvpath =os.path.join(".","Resources", "budget_data.csv")


# Introduce the variable to formulate the list
budget = []


# Create a csv utilizing the file path and populate list
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
    budget.append(csv_header)
    for row in csvreader:
        budget.append(row)

# Set variables for finding the net total and Month Count
# Count the rows starting from the second row
# Sum all the net totals together
Month_Count = 0
Net_Total = 0
for row in budget[1:]:
    Month_Count +=1
    Net_Total += int(row[1])


# Make a list of the monthly totals to use for analyse
Month_Total= [int(j) for i, j in budget[1:]]

# Zip the month total list to itself, one index ahead for one of the lists
# Subtract, find the difference betweeen the zipped items
Month_Change = [x - y for x, y in zip(Month_Total[1:], Month_Total)]


#



