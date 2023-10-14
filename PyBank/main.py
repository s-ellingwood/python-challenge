#import necessary modules
import os
import csv
from os.path import dirname, join

#------------------------------------------------------------------------
#establish that we're working out of the current folder/cwd location
current_dir = dirname(__file__)
csvpath = join(current_dir, "./Resources/budget_data.csv")

#------------------------------------------------------------------------
#using with open() to read the budget_data csv file into a list of dictionaries
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	print(csvreader)
	#reading and storing the header row
	csv_header = next(csvreader)
	data = []
	for row in csvreader:
		record = {}
		for i, value in enumerate(row):
			record[csv_header[i]] = value
		data.append(record)

#------------------------------------------------------------------------
#TOTAL NUMBER OF MONTHS INCLUDED IN THE DATASET
#creating list of month values given to the 'Date' key in data
dates = []
for item in data:
	month = item["Date"]
	dates.append(month)
#getting only those dates that are unique
dates_set = set(dates)
#getting the number of months
unique_dates = len(dates_set)

#------------------------------------------------------------------------
#NET TOTAL AMOUNT OF "PROFIT/LOSSES" OVER ENTIRE PERIOD
total = 0
for item in data:
	total = total + int(item['Profit/Losses'])

#------------------------------------------------------------------------
#CHANGES IN "PROFIT/LOSSES" OVER ENTIRE PERIOD
#getting just the values for the 'Profit/Losses' key
prof_loss = []
for item in data:
	money = int(item["Profit/Losses"])
	prof_loss.append(money)
#getting the difference between each value for the 'Profit/Losses' key
changes = []
for i in range(len(prof_loss)):
	difference = 0
	if i-1 < 0:
		difference = 0
	else:
		difference = int(prof_loss[i]) - int(prof_loss[i-1])
	changes.append(difference)
#getting the sum of the changes
totchange = 0
for item in changes:
	totchange = totchange + int(item)
#CALCULATING THE AVERAGE OF THOSE CHANGES
average_change = round(totchange/(len(changes)-1), 2)

#------------------------------------------------------------------------
#FINDING GREATEST INCREASE IN PROFITS (DATE AND AMOUNT) OVER THE ENTIRE PERIOD
#merging the dates and changes lists to get dates and changes into a single list
change_data = [list(l) for l in zip(dates, changes)]
#finding which month had the greatest increase from the previous month & the month of that increase
greatest_inc = 0
inc_month = ""
for item in change_data:
	if int(item[1]) > greatest_inc:
		greatest_inc = int(item[1])
		inc_month = item[0]

#------------------------------------------------------------------------
#FINDING GREATEST DECREASE IN PROFITS (DATE AND AMOUNT) OVER THE ENTIRE PERIOD
#still using the list created above (change_data)
#finding which month had the greatest decrease from the previous month & the month of that decrease
greatest_dec = 0
dec_month = ""
for item in change_data:
	if int(item[1]) < greatest_dec:
		greatest_dec = int(item[1])
		dec_month = item[0]

#------------------------------------------------------------------------
#PRINT FINANCIAL ANALYSIS
print("Financial Analysis")
print("----------------------")
print(f"Total Months: {unique_dates}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {inc_month} (${greatest_inc})")
print(f"Greatest Decrease in Profits: {dec_month} (${greatest_dec})")


#------------------------------------------------------------------------
#PRINT FINANCIAL ANALYSIS TO A .TXT FILE SAVED IN THE 'analysis' FOLDER
with open(join(current_dir, "./analysis/financial_analysis.txt"), 'w') as f:
	print("Financial Analysis", file=f)
	print("----------------------", file=f)
	print(f"Total Months: {unique_dates}", file=f)
	print(f"Total: ${total}", file=f)
	print(f"Average Change: ${average_change}", file=f)
	print(f"Greatest Increase in Profits: {inc_month} (${greatest_inc})", file=f)
	print(f"Greatest Decrease in Profits: {dec_month} (${greatest_dec})", file=f)