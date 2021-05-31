# Import - Voter Analysis
import os
import csv

# Variables
totalVotes = 0
khanVotes = 0
correyVotes = 0
liVotes = 0
otooleyVotes = 0

# Set Path
csvpath = os.path.join('Resources', 'election_data.csv')


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    for row in csvreader:
        
        # Total Number Of Votes Cast
        totalVotes += 1
        
        # Total Number Of Votes per Candidate 
        if (row[2] == "Khan"):
            khanVotes += 1
        elif (row[2] == "Correy"):
            correyVotes += 1
        elif (row[2] == "Li"):
            liVotes += 1
        else:
            otooleyVotes += 1
            
    # Percentage Of Votes per Candidate
    kahnPercent = khanVotes / totalVotes
    correyPercent = correyVotes / totalVotes
    liPercent = liVotes / totalVotes
    otooleyPercent = otooleyVotes / totalVotes
    
    # Winner Of The Election per Popular Vote
    winner = max(khanVotes, correyVotes, liVotes, otooleyVotes)

    if winner == khanVotes:
        winnerName = "Khan"
    elif winner == correyVotes:
        winnerName = "Correy"
    elif winner == liVotes:
        winnerName = "Li"
    else:
        winnerName = "O'Tooley" 

# Print Voter Analysis
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

# Path and Write Output File
output_file = os.path.join('Analysis', 'election_data_revised.txt')

with open(output_file, 'w',) as txtfile:

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