"""
Djeme Doli   12/04/2020
Program: DecimalToBinary 
         Converts any given decimal number into Binary
1. Input 
   Dec       # The Decimal number to convert into Binary
2. Variables
   Qot       # The 2 Interger division result
   Mod       # The 2 modilus division result
3. Output
   Bin       # The Binary equivalent of the Decimal number
4. Computation
   Qot = Dec // 2
   Mod = Dec % 2
"""

Qot = input("Please Enter a Decimal: ")
if Qot.isdigit():
   Qot = int(Qot)
   Bin = []
   while Qot != 0:
         Mod = Qot % 2
         Bin.append(Mod)
         Qot = Qot // 2
         

   Bin.reverse()
   DecBinary = ' '.join(map(str, Bin)) 
   print(DecBinary)
else:
  print("You have not entered a Decimal (Digits only)")

