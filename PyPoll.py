# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

import csv
dir(csv)
dir(int)

# Assigning a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'

# Open the elections result and read the file.
with open(file_to_load) as election_data: 

    # To do: perform analysis
    print(election_data)


import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the elections results and read the file
with open(file_to_load) as election_data:

    # Print the file object
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
    txt_file.write("Counties in the Election\n-------------------\nArapahoe\nDenver\nJefferson")

    # To do: read and analyze data here
   
# Open the election results and read the file.
with open(file_to_load) as election_data:   
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Print each row in the csv file
    #for row in file_reader:
        #print(row)
    headers = next(file_reader)
    print(headers)