import os,csv
from pathlib import Path


# Path to collect data from the Resources folder
budget_data_csv = os.path.join("budget_data.csv")

# def print_bankdata(dataRow):

#     # The total number of months included in the dataset
#     # total_no_of_months = len(dataRow[0])
#     # print (" The total number of months = " + total_no_of_months)
    # months = ','.join(dataRow[0])
    # print(months)
    
#     # The net total amount of "Profit/Losses" over the entire period
#     # The average of the changes in "Pro[fit/Losses" over the entire period
#     # The greatest increase in profits (date and amount) over the entire period
#     # The greatest decrease in losses (date and amount) over the entire period

#Create empty lists
total_months = []
total_profit = []
monthly_profit_change = []

# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # months_count = sum(1 for row in csvreader)
    # print (months_count)
    
    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    
    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
    # Obtain the max and min of the the montly profit change list
    max_increase_value = max(monthly_profit_change)
    max_decrease_value = min(monthly_profit_change)
    
    max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
    max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print Statements

print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output files
output_file = os.path.join("Analysis_Summary.txt")

with open(output_file,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
