#calculating  user’s monthly savings based on inputted monthly income and expenses

Monthly_income = int(input("Please Enter Your Monthly Income"))
Monthly_expenses = int(input("Please Enter Your Monthly Expenses"))

Monthly_savings = Monthly_income - Monthly_expenses
print("Your monthly savings are", Monthly_savings)

Projected_Savings =  Monthly_savings * 12 + Monthly_savings * 12 * 0.05

print("Your projected saving after one year with interest is", Projected_Savings)