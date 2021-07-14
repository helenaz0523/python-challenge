import os
import path
import csv

budgetdata_csv = os. path.join('Resources', 'budget_data.csv')
  # Create a text file for analysis


#Save path
analysisoutput= os.path.join('Analysis','analysisoutput.txt')
textfile= open("analysisoutput.txt",'x')
with open(budgetdata_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # COUNT THE ROW
    # skip the header
    header = next(csvreader)
    # create list for month and pl amo0unt
    months = []
    pllist = []

    itemcount = 0
  
    for row in csvreader:
        # assign the index to month and pl list
        month = row[0]
        pl = row[1]
        # fill the list created for month and pl
        months.append(month)
        pllist.append(pl)
        # Count the list item number
        itemcount = len(months)
    print("Financial Analysis",file=textfile)
    print("-----------------------------",file=textfile)
    print(f"Total Months: {itemcount}",file=textfile)
    # sum the Pl ampount in the list
    total = 0
    for i in range(itemcount):
        total = total+int(pllist[i])
    print(F"Total: $ {total}",file=textfile)

    # calculate the change between pl
    totalchange = 0
    monthlychange = 0
    increase = 0
    decrease =0 
    bestmonth = 0
    worstmonth= 0
    for j in range(itemcount-1):
        totalchange = totalchange+(float(pllist[j+1])-float(pllist[j]))
        Avg = round(totalchange/(itemcount-1), 2)
    print(F"Average  Change: $ {float(Avg)}",file=textfile)

    # locate the biggest increase
    for K in range(itemcount-1):
        monthlychange = float(pllist[K+1])-float(pllist[K])

        if (monthlychange > increase):
            increase = monthlychange
            bestmonth = K
        else:
            increase = increase

    print(f"Greatest increase in Profits: {months[bestmonth+1]} ({increase})",file=textfile)
 # Locate the biggest decrease
    for m in range (itemcount-1):
        monthlychange = float(pllist[m+1])-float(pllist[m])
        if (monthlychange < decrease):
            decrease = monthlychange
            worstmonth = m
        else:
            decrease = decrease
    print(f"Greatest dncrease in Profits: {months[worstmonth+1]} ({decrease})",file=textfile)
textfile.close()

