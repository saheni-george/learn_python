# program to calculate the change by a cashier in terms of 5's and 1's
amount_cashier = int(input('enter the amount by the customer '))
cash_fives = amount_cashier // 5
cash_ones = amount_cashier % 5
print(cash_ones)

print("the number of 5 notes is = ",cash_fives)
print("the number of 1 notes is = ",cash_ones)


