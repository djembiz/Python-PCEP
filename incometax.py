"""
Djeme Doli 11/30/2020
Program:taxform.py
Computes a person's income tax based on the gross income and number of dependants.
1. Constants
   tax_Rate
   std_Deduction
   perDependent_Deduction

2. Inputs # Variables
   gross_Income
   nbr_Dependents

3.Computations:
  taxable_Income = gross_Income - std_Deduction - total_dependent_Deduction
  income_Tax = taxable_Income * tax_Rate

4. Outputs
  income_Tax
"""
################################################################################

tax_Rate = 0.20
std_Deduction = 10000.0
perDependent_Deduction = 3000.0

while True: 
      gross_Income = input("Please, Enter gross income (yearly income): ")
      nbr_Dependents = input("How many dependants do you claim? ")

      if gross_Income.isdigit() and nbr_Dependents.isdigit():
         taxable_Income = float(gross_Income) - std_Deduction - float(nbr_Dependents) * std_Deduction
         break
      else:
          print("Enter numbers only for Gross Income and Number of Dependents")

income_Tax = float(taxable_Income) * tax_Rate
#print("Your Income Tax is: ",  "$" + str(income_Tax))
print(f"Your Income Tax is ${income_Tax} \n")




