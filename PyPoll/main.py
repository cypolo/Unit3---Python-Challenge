# import csv file thru liab
import os
import csv
# Define csv file's location
csvpath = os.path.join('Resources', 'election_data.csv')

#open csv file
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip headers row
    csv_header = next(csvreader,None)
    #print(csv_header)

    # Set empty list variables
    County= []
    Candidates = []
    CandidateWinner =[]
    VoteCount = []
    VotePercent =[]
    # Set Count # to Zero
    TotalCount = 0

# Loop thru each row
    for row in csvreader: 
        TotalCount += 1
        Candidates.append(row[2])
    for x in set(Candidates):
        CandidateWinner.append(x)
        VotesPerCandidte = Candidates.count(x)
        VoteCount.append(VotesPerCandidte)
        VotePercent.append(Candidates.count(x)/TotalCount)
        # Identify the max voted candidate
        Winner = CandidateWinner[VoteCount.index(max(VoteCount))]

    # output into text file
    with open('Election_Results' + '.txt', 'w') as text:
        text.write("Election Results"+"\n")
        text.write("----------------------------------------------------------\n")
        text.write("Total Vote: " + str(TotalCount) + "\n")
        text.write("----------------------------------------------------------\n")
        # Loop in Candidates pool, generate each candidate's vote count and percentage
        for i in range(len(set(Candidates))):
            text.write(CandidateWinner[i] + ": " + str(round(VotePercent[i]*100,1)) +"% (" + str(VoteCount[i]) + ")\n")
        text.write("----------------------------------------------------------\n")
        text.write("Winner: " + Winner +"\n")
        text.write("----------------------------------------------------------\n")







