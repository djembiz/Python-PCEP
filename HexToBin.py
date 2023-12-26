"""
Djeme Doli   12/04/2020
Program: HexToBinary 
         Converts any given Hexadecimal number into Binary

In this program, we use a base Hexa-Binary dictionary and convert any Hexadecimal numbers to binary

1. Constants
   

3. Variables
   Bin       # The Binary equivalent of the DeciHexadecimal number

"""


print("\n\n\tHexadecimal Numbers contain digits and any letter from A to F\n")

HexToBinary = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101',
                       '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
                       'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
Bin = []
Number = input("Please, Enter any Hexadecimal Number: ")
for digit in Number:

    Bin.append(HexToBinary[digit]) 

HexBinary = ''.join(map(str, Bin)) 

print(HexBinary)