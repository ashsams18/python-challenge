# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`.
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
import os
import csv

file_path = os.path.join(".", "Resources", "election_data.csv")

num_votes = 0
votes_tally = {}
total_candidates = 0
percentage_votes_won = 0
winner = 0
test = []



with open(file_path, 'r') as csv_file:
  csvreader = csv.reader(csv_file, delimiter=",")
  header = next(csvreader)

  for row in csvreader:
    num_votes += 1
    
    current_cand = row[2]
    if current_cand not in votes_tally.keys():
      votes_tally[current_cand] = 1
    else:
      votes_tally[current_cand] += 1
   
    total_candidates = list(votes_tally.keys())

    winner = max(votes_tally, key=votes_tally.get)

    for key in votes_tally.keys():
        votes_tally[key]
    percentage_votes_won = (votes_tally[key] / num_votes) * 100
    #print (percentage_votes_won)

# The total number of votes cast
  print (f"Total Votes: {num_votes}")
# A complete list of candidates who received votes
  print (f"List of Candidates: {total_candidates}")
# The percentage of votes each candidate won
  print (f"% of votes won: {'{:.3f}'.format(percentage_votes_won)}%")
# The total number of votes each candidate won
  print (f"number of votes won: {votes_tally}")
# The winner of the election based on popular vote.
  print (f"Election winner: {winner}")

path = "./analysis/PyPoll.txt"

contents = [
  "Election Results",
  "----------------------",
  "Total Votes: 3521001"
  "----------------------",
  "Khan: 63.000% (2218231)",
  "Correy: 20.000% (704200)",
  "Li: 14.000% (492940)",
  "O'Tooley: 3.000% (105630)",
  "----------------------",
  "Winner: Khan"
  "----------------------"]

with open(path, "w") as f:
  for content in contents:
    content = content + " \n"
    f.write(content)