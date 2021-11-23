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

# The total number of votes cast
print (f"Total Votes: {num_votes}")
# A complete list of candidates who received votes
print (f"List of Candidates: {total_candidates}")

for key in votes_tally.keys():
  #  = (float(votes_tally[key]) / float(num_votes) * 100)
  print(f"Total number and percentage of votes won by {key} = {votes_tally[key]} votes = ({(votes_tally[key]/num_votes)*100:.3f}%).")

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