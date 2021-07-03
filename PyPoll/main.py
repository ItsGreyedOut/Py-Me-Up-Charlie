# pybank python challenge
# GT Python Homework 07032021


# Time to begin, let's start with importing the OS and CSV file that we will use for this exercise analysis.
import os
import csv

# Path to collect data from the Resources folder
csvpath =os.path.join(".","Resources", "election_data.csv")

# Set initial variable to hold the total number of votes cast
Total_Votes = 0

# Set initial dictionary to hold the list of candidates and the total number of votes each candidate won
Candidate_Votes = {}

# Set initial variable to hold the winner of the election
Winner = "n/a"

# Set initial variable to hold the total number of votes the winner won
Winner_Votes = 0

# Read in the CSV file
with open(csvpath, newline="") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

        # Add one to the total number of votes cast
        Total_Votes += 1

        # Check if the name of the candidate is in the dictionary, if so...
        if row[2] in Candidate_Votes.keys():

            # Add one to the total number of votes the candidate won
            Candidate_Votes[row[2]] += 1

        # If the name of the candidate is not in the dictionary...
        else:

            # Add the candidate to the dictionary and set the total number of votes the candidate won to zero
            Candidate_Votes[row[2]] = 1

# Print out the election results
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(Total_Votes))
print("-------------------------")

# Loop through the candidate dictionary to calculate the winner of the election
for key in Candidate_Votes.keys():
    print(key + ": " + str(round((Candidate_Votes[key] / Total_Votes) * 100, 3)) + "% (" + str(Candidate_Votes[key]) + ")")

    # Check if the total number of votes the candidate won is greater than the total number of votes the winner won, if so...
    if Candidate_Votes[key] > Winner_Votes:

        # Set the winner of the election to the candidate
        Winner = key

        # Reset the total number of votes the winner won
        Winner_Votes = Candidate_Votes[key]

print("-------------------------")
print("Winner: " + Winner)
print("-------------------------")

# Export a text file with the results
analysisText = open("analysis.txt", 'w')

analysisText.write("Election Results\n")
analysisText.write("-------------------------\n")
analysisText.write("Total Votes: " + str(Total_Votes) + "\n")
analysisText.write("-------------------------\n")
for key in Candidate_Votes.keys():
    analysisText.write(key + ": " + str(round((Candidate_Votes[key] / Total_Votes) * 100, 3)) + "% (" + str(Candidate_Votes[key]) + ")\n")
analysisText.write("-------------------------\n")
analysisText.write("Winner: " + Winner + "\n")
analysisText.write("-------------------------")
