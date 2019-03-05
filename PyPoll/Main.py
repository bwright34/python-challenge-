

# Module for reading CSV files
import os
import csv
import operator

#Assign the variables
total_votes = 0
polls = {}

#Path to open CSV file
csvpath = os.path.join('election_data.csv')
with open(csvpath, 'r', newline = '') as csvfile:
   election_data = csv.reader(csvfile, delimiter= ',')

   #Skip the header row
   next(election_data, None)

   #Calculate the total number of votes cast
   #List of Polls who received votes
   #Calculate the total number of votes each candidate won
   for row in election_data:
       
       if row[2] not in polls.keys(): 
           polls[row[2]] = 1
       else:
           polls[row[2]] = polls[row[2]] + 1

   total_votes = 0

   for votes in polls.values():
       total_votes = total_votes + votes

   print("Election Results")
   print("--------------------------")
   print("Total Votes: " + str(total_votes))
   print("--------------------------")

#Path to export file as textfile
export_file = os.path.join("election_data.txt")
with open(export_file, 'w', newline='') as textfile:
   textfile.write("Election Results" "\n")
   textfile.write("--------------------------" "\n")
   textfile.write("Total Votes: " + str(total_votes) + "\n")
   textfile.write("--------------------------" "\n")

   #Calculate the percentage of votes each candidate won
   for name, votes in polls.items():
       percent= round((votes/total_votes) * 100, 3)
       percentage = "{:.3}".format(percent)
       print(name + " " + percentage + "% " + "(" + str(votes) + ")")
       textfile.write(name + " " + percentage + "% " + "(" + str(votes) + ")" + "\n")


#Winner based on voting
   print("--------------------------")
   textfile.write("--------------------------" "\n")
   winner = max(polls.items(), key=operator.itemgetter(1))[0]
   print("Winner: " + winner)
   textfile.write("Winner: " + winner)
