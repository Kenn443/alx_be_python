#calculating  user’s monthly savings based on inputted monthly income and expenses

income = int(input("Please Enter Your Monthly Income"))
expenses = int(input("Please Enter Your Monthly Expenses"))

savings = income - expenses
print("Your monthly savings are", savings)

Projected_Savings =  savings * 12 + savings * 12 * 0.05

print("Your projected saving after one year with interest is", Projected_Savings)