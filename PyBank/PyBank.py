## Challenge 1: PyBank

#* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `Profit/Losses`. 

#* Your task is to create a Python script that analyzes the records to calculate each of the following:
#       1.	The total number of months included in the dataset
#       2.	The total net amount of "Profit/Losses" over the entire period
#       3.	The average change in "Profit/Losses" between months over the entire period
#       4.	The greatest increase in profits (date and amount) over the entire period
#       5.	The greatest decrease in losses (date and amount) over the entire period
#* As an example, your analysis should look similar to the one below:

  #Financial Analysis
  #----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
 
#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#  import os and csv

import os
import csv

# set filepath

PyBankcsv = os.path.join("Resources","budget_data.csv")

# create lists for data  

profit = []
monthly_changes = []
date = []

# variables
 
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0



with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

  
    for row in csvreader:    
      # use count to count the number months in this dataset
      count = count + 1 

      # use for the greatest increase and decrease in profits
      date.append(row[0])

      # append the profit information & calculate the total profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      #calculate the avg change in profits month to month then calulate the avg change in profits
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit

      #store monthly changes in a list
      monthly_changes.append(monthly_change_profits)

      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit

      #calculate the average change in profits
      average_change_profits = (total_change_profits/count)
      
      #find the max and min change in profits and the corresponding dates these changes were obeserved
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")

 
