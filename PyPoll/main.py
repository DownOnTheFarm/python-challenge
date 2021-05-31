# Import - Voter Analysis
import os
import csv

# Variables
totalVotes = 0
khanVotes = 0
correyVotes = 0
liVotes = 0
otooleyVotes = 0

# Set Path For File
csvpath = os.path.join('Resources', 'election_data.csv')

# Open & Read CSV File
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    # Read Each Row Of Data After The Header
    for row in csvreader:
        
        # Calculate Total Number Of Votes Cast
        totalVotes += 1
        
        # Calculate Total Number Of Votes Each Candidate Won
        if (row[2] == "Khan"):
            khanVotes += 1
        elif (row[2] == "Correy"):
            correyVotes += 1
        elif (row[2] == "Li"):
            liVotes += 1
        else:
            otooleyVotes += 1
            
    # Calculate Percentage Of Votes Each Candidate Won
    kahnPercent = khanVotes / totalVotes
    correyPercent = correyVotes / totalVotes
    liPercent = liVotes / totalVotes
    otooleyPercent = otooleyVotes / totalVotes
    
    # Calculate Winner Of The Election Based On Popular Vote
    winner = max(khanVotes, correyVotes, liVotes, otooleyVotes)

    if winner == khanVotes:
        winnerName = "Khan"
    elif winner == correyVotes:
        winnerName = "Correy"
    elif winner == liVotes:
        winnerName = "Li"
    else:
        winnerName = "O'Tooley" 

# Print Analysis
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {totalVotes}")
print(f"---------------------------")
print(f"Kahn: {kahnPercent:.3%}({khanVotes})")
print(f"Correy: {correyPercent:.3%}({correyVotes})")
print(f"Li: {liPercent:.3%}({liVotes})")
print(f"O'Tooley: {otooleyPercent:.3%}({otooleyVotes})")
print(f"---------------------------")
print(f"Winner: {winnerName}")
print(f"---------------------------")

# Specify File To Write To
output_file = os.path.join('Analysis', 'election_data_revised.txt')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {totalVotes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {kahnPercent:.3%}({khanVotes})\n")
    txtfile.write(f"Correy: {correyPercent:.3%}({correyVotes})\n")
    txtfile.write(f"Li: {liPercent:.3%}({liVotes})\n")
    txtfile.write(f"O'Tooley: {otooleyPercent:.3%}({otooleyVotes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winnerName}\n")
    txtfile.write(f"---------------------------\n")