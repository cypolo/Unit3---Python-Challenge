# import csv file
import os
import csv
# Define csv file's location
csvpath = os.path.join('Resources', 'budget_data.csv')
# Open csv as reader
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip headers row
    csv_header = next(csvreader,None)

    # Declare variables and set them to Zeros
    MonthlyChange = []
    Date = []
    currentMonthProfit = 0
    lastMonthProfit = 0
    NumofMonths = 0
    TotalProfit = 0
    TotalProfitChange = 0
    AvgPLChange = 0
    GreatestIncrease = 0
    GreatestDecrease = 0
# First, run the variables for the FIRST row of data ONLY,
# in order to skip the first month's profit change calculation as first month's (Beg Bal - Zero) is not the realy monthly change amt
    for row in csvreader:
            NumofMonths += 1
            TotalProfit += int(row[1])
            lastMonthProfit = int(row[1])
            break
# now Loop thru the other rows, python will re-start from 3rd row (as header is the 1st row)
    for row in csvreader:
            Date.append(row[0])
            currentMonthProfit = int(row[1])
            TotalProfit += currentMonthProfit
            NumofMonths += 1
            ChangePerMonth = currentMonthProfit - lastMonthProfit
            MonthlyChange.append(ChangePerMonth)
            lastMonthProfit = currentMonthProfit

            #Average Monthly P&L Change Calc
            AvgPLChange = round(sum(MonthlyChange) / len(MonthlyChange),2)
            #Find Max and Min value in the MonthlyChange [set]
            GreatestIncrease = max(MonthlyChange)
            GreatestDecrease = min(MonthlyChange)

            #Based on Max and Min $ value, locate Date value in the Monthlychange index accordingly
            IncreaseDate = Date[MonthlyChange.index(GreatestIncrease)]
            DecreaseDate = Date[MonthlyChange.index(GreatestDecrease)]

    
    # output all the summary info into text
    with open('financial_analysis_report' + '.txt', 'w') as text:
        text.write('Financial Analysis'+"\n")
        text.write('-------------------------------'+"\n")
        text.write('Total Months: ' + str(NumofMonths) + "\n")
        text.write('Total Revenue: ' + str(TotalProfit) + "\n")
        text.write('Average Change: ' + str(AvgPLChange) +"\n")
        text.write('Greatest Increase in Profits: ' + IncreaseDate + "   " + "($" + str(GreatestIncrease) + ")" + "\n")
        text.write('Greatest Decrease in Profits: ' + DecreaseDate + "   " + "($" + str(GreatestDecrease) + ")" + "\n")
        