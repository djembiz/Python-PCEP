"""
Djeme Doli   12/04/2020
Program: DecimalToBinary 
         Converts any given Binary number into Decimal
"""

Bin = input("Enter a Binary number: ")
count = len(Bin)
Dec = 0
for digit in Bin:
    Dec += int(digit) * 2 ** (count -1)
    count -= 1
print(f"\n\nThe Decimal equivalent of {Bin} is {Dec}")
