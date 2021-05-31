# Import - Financial Analysis

import os
import csv

# Path

csvpath = os.path.join('Resources', 'budget_data.csv')

# Variables 
totalMonths = 0
totalRevenue =0
changes =[]
dateCount = []
greatest_inc = 0
greatest_incMonth = 0
greatest_dec = 0
greatest_decMonth = 0

# Open the CSV
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)
# Total Revenue and Months of Data
    previousProfit = int(row[1])
    totalMonths = totalMonths + 1
    totalRevenue = totalRevenue + int(row[1])
    greatest_inc = int(row[1])
    greatest_incMonth = row[0]

    for row in csvreader:
 
        totalMonths = totalMonths + 1
        totalRevenue = totalRevenue + int(row[1])

        # Calculate change Month over Month
        change = int(row[1]) - previousProfit
        changes.append(change)
        previousProfit = int(row[1])
        dateCount.append(row[0])
        
        # Greatest Inc.
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])
            greatest_incMonth = row[0]
            
        # Greatest Dec.
        if int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            greatest_decMonth = row[0]  
      
    # Grab Avgs. and Dates
    avgChange = sum(changes)/len(changes)

    high = max(changes)
    low = min(changes)

    # Print Analysis
    print("Financial Analysis")
    print("Total Months: " + str(totalMonths))
    print("Total Amount: " + str(totalRevenue))
    print(avgChange)
    print(greatest_incMonth, max(changes))
    print(greatest_decMonth, min(changes))

# Save Path and Output File

output_file = os.path.join('Analysis', 'budget_data_revised.txt')
with open(output_file, 'w',) as txtfile:
    PyBank = open(output_file,"w")
    PyBank.write("Financial Analysis") 
    PyBank.write('\n' +"Total Months" + str(totalMonths)) 
    PyBank.write('\n' +"Total Amount" + str(totalRevenue)) 
    PyBank.write('\n' +"Average" + str(avgChange)) 
    PyBank.write('\n' +greatest_incMonth) 
    PyBank.write('\n' +str(high))
    PyBank.write('\n' +greatest_decMonth) 
    PyBank.write('\n' +str(low))