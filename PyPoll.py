# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a varible to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    #To do: read and anylyze the data here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
# Print each row in csv file
    #for row in file_reader:
        #print(row)
    header = next(file_reader)
    print(header)



# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received the votes
# 3. The percentage of votes each candidate received
# 4. Total number of votes each candidate received
# 5. The winner of elections based on popular vote


