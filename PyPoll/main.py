# Import - Voting Analysis
import os 
import csv

# Path
csvpath = os.path.join('Resources', 'election_data.csv')

# Variables 
pollData={}
totalVotes = 0
with open(csvpath, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread, None)

    for row in csvread:
        totalVotes += 1
        if row[2] in pollData.keys():
            pollData[row[2]] = pollData[row[2]] + 1
        else:
            pollData[row[2]] = 1 
    

candidates = []  
totalVoters = []
# Total Number of votes
for key, value in pollData.items():
    candidates.append(key)
    totalVoters.append(value)
  
# Percentage of votes
percentageVotes =[]
for n in totalVoters:
    percentageVotes.append(round(n/totalVotes * 100, 1))
 
# Finding the winner
clean_data = list(zip(candidates, totalVoters, percentageVotes))

winnerList = []
for name in clean_data:
    if max(totalVoters) == name[1]:
        winnerList.append(name[0])
winner = winnerList[0]

# Print all data
print ("Election results :")
print(totalVotes) 
print(candidates)  
print(percentageVotes)
print(totalVoters)  
print(winner)

# Writng output files

output_file = os.path.join('Analysis', 'election_data_revised.txt')
with open(output_file, 'w',) as txtfile:
    PyPoll = open(output_file,"w")
    PyPoll.write("Election Results")  
    PyPoll.write('\n' + "Total_votes" + str(totalVotes)) 
    PyPoll.write('\n' + str(candidates))
    PyPoll.write('\n' + str(percentageVotes))
    PyPoll.write('\n' + str(totalVoters)) 
    PyPoll.write('\n' + "Winner:" + winner)    