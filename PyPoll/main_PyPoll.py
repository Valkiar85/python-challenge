# PyPoll

import os
import csv

# Import File

csvpath = os.path.join("Resources","election_data.csv")

# Pass the CSV file to a list

voters_list = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    # delete the header
    next(csvreader)
    for row in csvreader:
        voters_list.append(row)
        
# The total number of votes cast

total_v_cast = len(voters_list) 

# A complete list of candidates who received votes

candidates = [x[2] for x in voters_list]
candidates = set(candidates)

# Number of Votes received for each candidate

votes_correy = 0
votes_khan = 0
votes_li = 0
votes_otool = 0

for x in voters_list:
    
    if x[2] == 'Correy':
        votes_correy += 1
    if x[2] == 'Khan':
        votes_khan += 1
    if x[2] == 'Li':
        votes_li += 1
    if x[2] == "O'Tooley":
        votes_otool += 1 

# The percentage of votes each candidate won

percentage_correy = 0
percentage_khan = 0
percentage_li = 0
percentage_otooley = 0

# Correy

percentage_correy = votes_correy/total_v_cast

# Khan

percentage_khan = votes_khan/total_v_cast

# Li

percentage_li = votes_li/total_v_cast

# O'Tooley

percentage_otooley = votes_otool / total_v_cast

a = ["Correy","Khan","Li","O'Tooley"]

b = [votes_correy,votes_khan,votes_li,votes_otool]

zip(a,b)

candidate_votes = list(zip(a,b))

numbvotes = 0
winner = ""

for x in candidate_votes:
    if x[1] > numbvotes:
        numbvotes = x[1]
        winner = x[0]

# Voting Analysis

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_v_cast}")
print("-------------------------")
print(f"Khan: {percentage_khan:0.3%} ({votes_khan})")
print(f"Correy:{percentage_correy:0.3%} ({votes_correy})")
print(f"Li: {percentage_li:0.3%} ({votes_li})")
print(f"O'Tooley: {percentage_otooley:0.3%} ({votes_otool})")
print("-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

# Export Analysis to a Text File

external_file = os.path.join("Resources","voting_results.txt")

with open(external_file, 'w') as writetxt:
    writetxt.writelines("Election Results")
    writetxt.writelines("-------------------------")
    writetxt.writelines(f"Total Votes: {total_v_cast}")
    writetxt.writelines("-------------------------")
    writetxt.writelines(f"Khan: {percentage_khan:0.3%} ({votes_khan})")
    writetxt.writelines(f"Correy:{percentage_correy:0.3%} ({votes_correy})")
    writetxt.writelines(f"Li: {percentage_li:0.3%} ({votes_li})")
    writetxt.writelines(f"O'Tooley: {percentage_otooley:0.3%} ({votes_otool})")
    writetxt.writelines("-------------------------")
    writetxt.writelines(f"Winner: {winner}")
    writetxt.writelines(f"-------------------------")


















