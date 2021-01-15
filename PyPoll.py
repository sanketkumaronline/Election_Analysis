# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a varible to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    header = next(file_reader)

    # Print each row in heade file
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1 
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_options:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
     # Calculate the percentage of votes.      
    vote_percentage = float(votes) / float(total_votes) * 100
    #print out each candidate's name, vote count, and percentage of
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    if votes > winning_count and vote_percentage > winning_percentage:
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-----------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------------------------\n")
print(winning_candidate_summary)






# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received the votes
# 3. The percentage of votes each candidate received
# 4. Total number of votes each candidate received
# 5. The winner of elections based on popular vote


