import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath, 'r') as budget_data_csv:
    csvreader = csv.reader(budget_data_csv,delimiter=',')
    csv_header = next(csvreader)
    Total = 0
    TM = 0
    IP = 0
    DP = 0
    CC = 0
    CP = 0
    PP = 0
    TPC = 0
    PIP = 0
    PDP = 0
    TPC = 0
    Avg = 0
    for row in csvreader:
        TM += 1
        Total += int(row[1])
        CP = int(row[1])
        if TM > 1:
            CC = CP - PP
        if CC > PIP:
            PIP = CC
            PIPDate = row[0]
        if CC < PDP:
            PDP = CC     
            PDPDate = row[0]                                    
        TPC = CC + TPC
        PP = CP
    Avg = TPC/(TM-1)

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(TM))
    print("Total: $" + str(Total))
    print("Average  Change: $" + str(Avg))
    print("Greatest Increase in Profits: " + PIPDate +" ($" + str(PIP) + ")")   
    print("Greatest Decrease in Profits: " + PDPDate +" ($" + str(PDP) + ")") 
    output_path = os.path.join('Resources',"bank_result.csv")
    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Total Months: ',TM])
        csvwriter.writerow(['Total: $',Total])
        csvwriter.writerow(['Average  Change: $',Avg])       
        csvwriter.writerow(["Greatest Increase in Profits:",PIP])
        csvwriter.writerow(["Greatest Decrease in Profits",PDP])    