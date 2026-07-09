principal = float(input("Enter Principal Amount: "))
time = float(input("Enter Time (Years): "))
Rate = float(input("Enter Rate: "))
amount = principal * (1 + Rate / 100) ** time
compound_interest = amount - principal
print("Compound Interest =", compound_interest)
print("Total Amount =", amount)