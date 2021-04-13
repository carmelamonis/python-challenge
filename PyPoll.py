import csv
csvpath = ('../PyPoll/election_data.csv')
#csvpath = PyPoll.

totalVotes = 0
votes = []

with open(csvpath, 'r') as polldata:
    csv_reader = csv.reader(polldata, delimiter=',')
    header = next(csv_reader)
    #csv_reader is a list of lists
    #candidates = set(csv_reader)
    for line in csv_reader:
        #print(line)
        votes.append(line)
        totalVotes +=1


candidates = set({})
for vote in votes:
    #print(vote)
    candidates.add(vote[2])

#candidates = set(votes[2])
#print(candidates)

#candidate = [print(candidate) for candidate in candidates]



#List out print statements
print("Election Results")
print("------------------------")
print(f"Total Votes: {totalVotes}")
print("------------------------")

#Create a dictionary to get the values of the votes per candidate
candidateVotes = {}
for candidate in candidates: 
    candidateCounter = 0
    for vote in votes:
  
        if vote[2] == candidate:
            candidateCounter += 1
    candidateVotes[candidate] = candidateCounter



def winner(dictionary):
    value = dictionary.values()
    keys = dictionary.keys()
    maxValue = max(value)
    for key in keys:
        if dictionary[key] == maxValue:
            return key


#Sorting the existing dictionary
#sortedVotes = (key: value for key, value in sorted(candidateVotes.items(), key=lambda item: item[1], reverse=True))
#print(sortedVotes)
#print({key: value for key, value in sorted(candidateVotes.items(), key=lambda item: item[1], reverse=True)})
sortedVotes = sorted(candidateVotes.items(), key=lambda item: item[1], reverse=True)
#print(sortedVotes)
for candidate in sortedVotes:
    print(f"{candidate[0]}: {format(round((int(candidate[1])/totalVotes)*100, 3),'.3f')}% ({candidate[1]})")
          

#print(candidateVotes)
print("------------------------")
print(f"Winner: {winner(candidateVotes)}")
print("------------------------")

