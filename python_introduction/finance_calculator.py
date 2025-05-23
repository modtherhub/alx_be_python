# This script will calculate the user’s monthly savings based on inputted monthly income and expenses. 
# It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.


user_monthly_income = int(input("Enter your monthly income: "))
user_monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = user_monthly_income - user_monthly_expenses

# a simple annual interest rate of 5%.

projected_saving = monthly_savings * 12 + (monthly_savings * 12 * .05)

print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_saving}")