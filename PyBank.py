import csv

#Create a new list to hold all the records that were in the file
newList=[]

#Gets the total budget. Initialized at 0
totalBudget = 0

#Count the number of months.
totalMonths = 0

with open('budget_data.csv', 'r') as budget_data:
    csv_reader = csv.reader(budget_data, delimiter =",")
    
    #Skips the first line with the header
    header = next(budget_data)

    #adds records in the new list & adds the budget cost to the totalBudget variable
    for line in csv_reader:
        totalBudget += int(line[1])
        newList.append(line)
        #Adds 1 to the totalMonths counter to count the total of "lines" in the file
        totalMonths += 1

#Gets the total number of records in the list for the number of months
#totalMonths = len(newList)
#print(newList)

#Create a function to get the average given a dictionary
def average(dictionary):
  #dictionary.values() returns a tuple of the values
  total = sum(dictionary.values())
  length = len(dictionary.values())
  return total/length

#Create a dictionary to add the values of the changes, with the keys as the months. 
monthlyChanges = {}

#-1 because there will be no change comparison for last value
for i in range(len(newList)-1):
    #calculates the difference of the next month witht he current month
    budgetChange = int(newList[i+1][1]) - int(newList[i][1])
    
    #adds key + value to the new dictionary
    #key is the  month of the following month
    #value is the difference between following & current month
    monthlyChanges[newList[i+1][0]] = budgetChange

#create a function to get the maximum within a dictionary by looking through the values
def maxKey(dictionary):
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    maxValue = max(values)
    for key in keys:
        if dictionary[key] == maxValue:
            return key

#create a function to get the minimum within a dictionary by looking through the values
def minKey(dictionary):
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    minValue = min(values)
    for key in keys:
        if dictionary[key] == minValue:
            return key

#Print out all the data
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months:  {totalMonths}")
print(f"Total: ${totalBudget}")

#Takes the average of the values in the monthlyChanges dictionary, and round it 2 decimals
print(f"Average Change: ${round(average(monthlyChanges), 2)}")

#max/minKey returns the key of the maximum value in monthlyChanges dictionary
#Then take that key and returns the value of that key
print(f"Greatest Increase in Profits: {maxKey(monthlyChanges)} (${monthlyChanges[maxKey(monthlyChanges)]})")
print(f"Greatest Decrease in Profits: {minKey(monthlyChanges)} (${monthlyChanges[minKey(monthlyChanges)]})")
#print(monthlyChanges.values())