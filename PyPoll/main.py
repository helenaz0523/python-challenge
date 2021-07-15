import os
import path
import csv

# open the CSV file
electiondata_csv= os.path.join("Resource","election_data.csv")
# Create a text file for analysis output
# Save text file path
analysisoutput2= os.path.join('Analysis','analysisoutput2.txt')
textfile2= open("analysisoutput2.txt",'x')
# Read the CSV file
with open(electiondata_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # skip the header
    header = next(csvreader)
    # create list for Votes Column  , Candidates column , unique candidates, and the votes for each unique candidate, and % for votes for each candidate
    Votes=[]
    Candidates=[]
    Uniquecandidates=[]
    Voteeach=[]
    Voteeachpc=[]

    #COUNT THE VOTES 
    itemcount = 0
    for row in csvreader:
        # assign the index to vote
        vote = row[0]
        candidate =row[2]
        # fill the list created for Votes
        Votes.append(vote)
        Candidates.append(candidate)
        # Count the list item number
        itemcount = len(Votes)
    print("Election Results")
    print("Election Results", file=textfile2)
    print("-----------------------------")
    print("-----------------------------", file=textfile2)
    print(f"Total Votes: {itemcount}")
    print(f"Total Votes: {itemcount}", file=textfile2)

    #count how many candidates
    # Take the first row in Candidates lit 
    Uniquecandidates.append(Candidates[0])
   
    for i in range(itemcount-1):
        if Candidates[i+1] != Candidates[i] and Candidates[i+1] not in Uniquecandidates:
             Uniquecandidates.append(Candidates[i+1])
    n= len(Uniquecandidates)
    # CHECK CANDIDATES
    #print([Uniquecandidates])
    # print candidates numbers, 
    #print(f"Total Candidates: {n}")

# COUNT THE VOTES BY EACH unqiue CANDIDATE
    for j in range(n):
        Voteeach.append(Candidates.count(Uniquecandidates[j]))
    #print(Voteeach) 
# Calculate the % for each candidate's votes
    for k in range(n):
        Voteeachpc.append(f'{round((Voteeach[k]/itemcount*100),4)}%')
    #print(Voteeachpc)
    #Zip the lists together and print the zip out
    Result= zip(Uniquecandidates,Voteeach,Voteeachpc)
    Result=set(Result)
    print(Result)
    print(Result,file=textfile2)


 # ZIp the list together
 #Result = zip(Uniquecandidates, Votecan)
 #print (Result)