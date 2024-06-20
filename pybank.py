import pandas as pd

# Loading the csv
df_budget = pd.read_csv(r"C:\Users\karki\Downloads\Starter_Code (4)\Starter_Code\PyBank\Resources\budget_data.csv")

# calculating the unique months
total_months = df_budget['Date'].nunique()

# calculating the total profit/loss
total_amount = df_budget['Profit/Losses'].sum()

# Calculating the average change in profit
df_budget['Profit_Change'] = df_budget['Profit/Losses'].diff()
average_change = df_budget['Profit_Change'].mean()

# finding the greatest increase and decrease in profit
greatest_increase = df_budget.loc[df_budget['Profit_Change'].idxmax()]
greatest_increase
greatest_decrease = df_budget.loc[df_budget['Profit_Change'].idxmin()]
greatest_decrease

# Print the financial analysis
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f"Total: ${total_amount}")
print(f'Average Change: ${average_change:.2f}')
print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Profit_Change']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Profit_Change']})")





