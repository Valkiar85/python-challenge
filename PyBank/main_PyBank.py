import os
import csv

# Read the csv file

csvpath = os.path.join("Resources", "budget_data.csv")

# Pass the csv file to a list

budget_list = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    # delete the header
    next(csvreader)
    for row in csvreader:
        budget_list.append(row)

# The total number of months included in the dataset

budget_months = len(budget_list)

# months date

months_date = [x[0] for x in budget_list]

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


# Pass the profit/losses to a new list, make them integers

budget_amount = [x[1] for x in budget_list]
budget_amount = [int(x) for x in budget_amount]

# The net total amount of "Profit/Losses" over the entire period

profits = 0

for profit in budget_amount:
    profits += profit

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

changes = []

for x in range(len(budget_amount) - 1):
    r = budget_amount[x+1] - budget_amount[x]
    changes.append(r)

# Find average of those changes

average = sum(changes)/len(changes)

# The greatest increase in profits (date and amount) over the entire period

min_change = min(changes)

months_date = []

for x in budget_list:
    months_date.append(x[0])

# The greatest increase in losses (date and amount) over the entire period

date_greatest_increase = months_date[budget_amount.index(max(budget_amount))]
budget_max_change = max(changes)

# The greatest decrease in losses (date and amount) over the entire period

date_greatest_decrease = months_date[budget_amount.index(min(budget_amount))]
budget_min_change = min(changes)

# Financial Analysis

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {budget_months}')
print(f'Total: ${profits}')
print(f'Average  Change: ${average}')
print(f'Greatest Ipythonncrease in Profits: {date_greatest_increase} (${budget_max_change})')
print(f'Greatest Decrease in Profits: {date_greatest_decrease} (${budget_min_change})')

# Export Analysis to a Text File

external_file = os.path.join("Resources","analysis_results.txt")

with open(external_file, 'w') as writetxt:
    writetxt.writelines("Financial Analysis")
    writetxt.writelines("----------------------------")
    writetxt.writelines(f'Total Months: {budget_months}')
    writetxt.writelines(f'Total: ${profits}')
    writetxt.writelines(f'Average  Change: ${average}')
    writetxt.writelines(f'Greatest Increase in Profits: {date_greatest_increase} (${budget_max_change})')
    writetxt.writelines(f'Greatest Decrease in Profits: {date_greatest_decrease} (${budget_min_change})')
    




