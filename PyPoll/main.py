#import necessary modules
import os
import csv
from os.path import dirname, join

#------------------------------------------------------------------------
#establish that we're working out of the current folder/cwd location
current_dir = dirname(__file__)
csvpath = join(current_dir, "./Resources/election_data.csv")

#------------------------------------------------------------------------
#using with open() to read the budget_data csv file into a list of dictionaries
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	print(csvreader)
    #reading and storing the header row
	csv_header = next(csvreader)
	data = []
	for row in csvreader:
		record = {}
		for i, value in enumerate(row):
			record[csv_header[i]] = value
		data.append(record)
		
#------------------------------------------------------------------------
#TOTAL NUMBER OF VOTES CAST
#creating list of ballot ID values given to the 'Ballor ID' key in data
total_votes = []
for item in data:
	voter_id = item["Ballot ID"]
	total_votes.append(voter_id)
#getting only those ballot ids that are unique
votes_set = set(total_votes)
#getting the number of votes cast
unique_votes = len(votes_set)

#------------------------------------------------------------------------
#COMPLETE LIST OF CANDIDATES WHO RECEIVED VOTES
#using set() to find the unique values given to the 'Candidate' key in the dataset
candidates = set(d["Candidate"] for d in data)

#------------------------------------------------------------------------
#TOTAL NUMBER OF VOTES EACH CANDIDATE WON
#importing the necessary module
import collections
#using collections.Counter to find the number of votes for each unique value of the 'Candidate' key
candidates_count = collections.Counter(e['Candidate'] for e in data)
#defining variables for the number of votes for each candidate
CCS_number = candidates_count["Charles Casper Stockham"]
DD_number = candidates_count["Diana DeGette"]
RAD_number = candidates_count["Raymon Anthony Doane"]

#------------------------------------------------------------------------
#PERCENTAGE OF VOTES EACH CNADIDATE WON
#using the number of votes for each candidate from above as well as the total number
#of votes (unique_votes) to find the percentage of votes each candidate won
CCS_percent = round((CCS_number/unique_votes)*100, 3)
DD_percent = round((DD_number/unique_votes)*100, 3)
RAD_percent = round((RAD_number/unique_votes)*100, 3)

#------------------------------------------------------------------------
#WINNER OF THE ELECTION BASED ON POPULAR VOTE
#using a for loop to loop through each key: value pair in the candidates_count dictionary
#if the number of votes for a candidate is greater than any of the candidates prior, it saves
#the current candidate's name as the value for winner
winner_num = 0
winner = ""
for item in candidates_count.items():
	if int(item[1]) > winner_num:
		winner_num = int(item[1])
		winner = item[0]


#------------------------------------------------------------------------
#PRINT ELECTION RESULTS TO TERMINAL
print("Election Results")
print("---------------------")
print(f"Total Votes: {unique_votes}")
print("---------------------")
print(f"Charles Casper Stockham: {CCS_percent}% ({CCS_number})")
print(f"Diana DeGette: {DD_percent}% ({DD_number})")
print(f"Raymon Anthony Doane: {RAD_percent}% ({RAD_number})")
print("---------------------")
print(f"Winner: {winner}")
print("---------------------")

#------------------------------------------------------------------------
#PRINT ELECTION RESULTS TO A .TXT FILE SAVED IN THE 'analysis' FOLDER
with open(join(current_dir, "./analysis/election_results.txt"), 'w') as f:
	print("Election Results", file=f)
	print("---------------------", file=f)
	print(f"Total Votes: {unique_votes}", file=f)
	print("---------------------", file=f)
	print(f"Charles Casper Stockham: {CCS_percent}% ({CCS_number})", file=f)
	print(f"Diana DeGette: {DD_percent}% ({DD_number})", file=f)
	print(f"Raymon Anthony Doane: {RAD_percent}% ({RAD_number})", file=f)
	print("---------------------", file=f)
	print(f"Winner: {winner}", file=f)
	print("---------------------", file=f)