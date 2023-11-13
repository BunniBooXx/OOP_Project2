# def function 
# if and else statements
#company named Bigger Pockets 
# client Brandon
# ROI for rental property (return on investment)
# asking for an automated Rental Property Calculator.
# 1 Income 
##############
#Rental = 2000 per month
#Laundry= 0
#Storage = 0 
#misc= 0 
#total = 2000/ per month
#2 Expenses 
#############
#Tax = $150 
#Insurance = $100
#Utilities = $0
  #electric,water,sewer,garbage,gas
# HOA fees = $0
#lawn or snow care = $0
#vacancy = $100
#repairs = $100/month
#capital expenditures = $100
# propery mortgage = $200/month (10% of rent)
# mortgage = 860.00
# total monthly expenses = 1610

# 3 Cash Flow
##########
#Income - Expenses 
#$2,000 - $1,610
#total monthly cashflow = $390

#4 Cash on Cash ROI 
#####################
# Down Payment = $40,000
# Closing Costs = $3,000
# Rehab budget = $7,000 
# misc other = $0
# Total Investments = $50,000
# monthly cash flow x 12(1 year) = 4,680
# annual cash flow (4,680)// total investment (50,000) = 9.36 % (cash on cash ROI)

#### 
# self init class 
# self.etc is a class 
# 

class ROI():
    def __init__(self, income, expenses):
        self.income = income
        self.expenses = expenses

    def total_income(self):
        return self.income

    def total_expenses(self):
        return self.expenses

    def total_roi(self, user_income, user_expenses):
        return user_income - user_expenses

# Get user input for income and expenses
user_income = float(input("Enter your total Monthly Income: "))
user_expenses = float(input("Enter your total monthly expenses and investment: "))

# Create an instance of the ROI class
calc = ROI(2000, 1000)

# Calculate and print the ROI
result = calc.total_roi(user_income, user_expenses)
print(f"Your total ROI is: {result}")










       
