import os
import csv
candidates = []
TotalVotes = 0
K = 0
C = 0
L = 0
O = 0
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, 'r') as election_data_csv:
    csvreader = csv.reader(election_data_csv,delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        TotalVotes += 1
        if row[2] == "Khan":
            K +=1
        elif row[2] == "Correy":
            C +=1
        elif row[2] == "Li":
            L +=1
        elif row[2] == "O'Tooley":
            O +=1
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(TotalVotes))
print("-------------------------")
KVP = K/TotalVotes*100
print("Khan: " + str(round(KVP,2)) +"00%"+ " ("+ str(K)+ ")")
CVP = C/TotalVotes*100
print("Correy: " + str(round(CVP,2)) +"0%"+ " ("+ str(C)+ ")")
LVP = L/TotalVotes*100
print("Li: " + str(round(LVP,2)) +"00%"+ " ("+ str(L)+ ")")
OVP = O/TotalVotes*100
print("O'Tooley: " + str(round(OVP,2)) +"00%"+ " ("+ str(O)+ ")")
print("-------------------------")
output_path = os.path.join('Resources',"polls_result.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Candidate', 'Votes'])
    csvwriter.writerow(['Khan',K])
    csvwriter.writerow(['Correy',C])
    csvwriter.writerow(['Li',L])       
    csvwriter.writerow(["O'Tooley",O])
    csvwriter.writerow(["Total Votes",TotalVotes])    