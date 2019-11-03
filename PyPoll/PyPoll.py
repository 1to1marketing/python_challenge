import os
import csv
CandField = []
candidates = {"Candidates":"","Votes":0}
TV = 0
csvpath = os.path.join('Resources', 'election_data_test.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    sortedlist = sorted(csvreader, key=(2), reverse=False)
    print(sortedlist)
    # for row in csvreader:
    #     TV += 1
    #     print(str(TV))
    #     if row[2] in CandField:
    #       print('Yes') 
    #       candidates[1] += 1
    #     else:
    #         print('No')
    #         CandField.append(row[2])
    #         candidates = {'Name': row[2],'Vote':1}

# print(candidates)
# print(CandField)
# print("Election Results")
# print("-------------------------")
# print("Total Votes: " + str(TV))
# print("-------------------------")
# print("Khan:")
# print("-------------------------")

