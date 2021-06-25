# Problem Set 2
# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

# def ccBalance(balance, annualInterestRate, monthlyPaymentRate):

# iterate over 12 months:
    # minimum payment is balance times minimum montly payment rate
    # unpaid balance is balance minus minimum payment 
    # interest is unpaid balance times annual interest rate divided by 12 months
    # balance value is updated and goes all over the same loop again

# output balance (which is the remaning balance)

annualInterestRate = 0.18
monthlyPaymentRate = 0.02
balance = 5000.00
numMonths = 12.0

while numMonths <= 12.0 and numMonths > 0:
    minimumPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minimumPayment
    interest =  annualInterestRate / 12.0 * unpaidBalance
    balance = unpaidBalance + interest
    numMonths -= 1.0
print(round(balance, 2))
