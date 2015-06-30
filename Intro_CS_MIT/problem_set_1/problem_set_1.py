# Problem Set 1 [Paying off Credit Card Debt] from MIT Intro to CS 6.00
# Name:Vivian D
# Time Spent: 45 mins

#Problem 1, Paying the Minimum
"""
Use raw_input() to ask for the following three floating point numbers:
1.
the outstanding balance on the credit card
2.
annual interest rate
3.
minimum monthly payment rate

For each month, print the minimum monthly payment, remaining balance,
principle paid in the format shown in the test cases below.
All numbers should be rounded to the nearest penny. Finally, print the result,
which should include the total amount paid that year and the remaining balance.

format:
Enter the outstanding balance on your credit card: 4800
Enter the annual credit card interest rate as a decimal: .2
Enter the minimum monthly payment rate as a decimal: .02
Month: 1
Minimum monthly payment: $96.0
Principle paid: $16.0
Remaining balance: $4784.0
Month: 2
Minimum monthly payment: $95.68
Principle paid: $15.95
Remaining balance: $4768.05
"""
# Taking inputs from users
balance = float(raw_input("Please enter the outstanding balance on your credit card: "))
annual_int_rate = float(raw_input("Please enter the annual credit card interest rate as a decimal: "))
min_pay_rate = float(raw_input("Please enter the minimum monthly payment rate as a decimal: "))

# defining initial value
month = 0
tot_paid = 0

# computation of the payments for a calendar year
for itr in range(1, 13):
    month += 1
    min_payment = min_pay_rate * balance
    interest_paid = (annual_int_rate/12.0 * balance)
    principle_paid = min_payment - interest_paid
    balance -= principle_paid
    tot_paid += principle_paid + interest_paid

    print "Month: " + str(month)
    print "mininum monthly payment: " + "$" + str(round(min_payment, 2))
    print "Principle paid: " + "$" + str(round(principle_paid, 2))
    print "Your remaining balance: " + "$" + str(round(balance, 2))

print "RESULT: "
print "Total Amount Paid: " + "$" + str(round(tot_paid, 2))
print "Your Remaining Balance: " + "$" + str(round(balance, 2))



