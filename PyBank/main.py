# Your task is to create a Python script that analyzes the records to calculate each of the following:
import os
import csv

file_path = os.path.join(".", "Resources", "budget_data.csv")
num_rows = 0
net_total = 0
current = 0
previous = 0
change = 0
sum_all_changes = 0
count_all_changes = 0
should_count = False
greatest_value = 0
greatest_month = ""

with open(file_path, 'r') as csv_file:
  csvreader = csv.reader(csv_file, delimiter=",")
  header = next(csvreader)

# The total number of months included in the dataset
  for row in csvreader:
    num_rows += 1
    # The net total amount of "Profit/Losses" over the entire period
    # row[1]
    net_total = int(row[1])+net_total
    # print(type(row[1]))
    current = int(row[1])
    
    change = current - previous
    previous = current
    
    if should_count:
      #print("Summing", change)
      sum_all_changes += change
      count_all_changes += 1
    else:
      should_count = True
    
    if change > greatest_value:
      greatest_value = change
      greatest_month = row[0]

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

# text
  # Financial Analysis
  # Total Months: 86
  print (f"Total Months: {num_rows}")
  # Total: $38382578
  print(f"Total : ${net_total}")
  # # Average  Change: $-2315.12
  print(f"Average Change : ${round(sum_all_changes / count_all_changes, 2)}")
  # # Greatest Increase in Profits: Feb-2012 ($1926159)
  print(f"Greatest Increase in Profits : {greatest_month} | ${greatest_value}")
  # # Greatest Decrease in Profits: Sep-2013 ($-2196167)
  # print(f"Greatest Decrease in Profits : {net_total}")
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
