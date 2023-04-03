# for the required gross income values from the user we  assign two float inputs
gross_income = float(input("Enter gross income: "))
num_dependents = float(input("Enter number of dependents: "))

# these are the required equations as per the question
standard_deduction = 10000
dependent_deduction = 3000
taxable_income = gross_income - standard_deduction - (dependent_deduction * num_dependents)
tax_rate = 0.2  # 20%=20/100*100=0.2
income_tax = taxable_income * tax_rate

# print the result using '/.' operator to easily get the requisite solution with separations
print("Taxable income: $", format(taxable_income, ".2f"), sep="")
print("Income tax: $", format(income_tax, ".2f"), sep="")
