"""
Djeme Doli 12/10/2020
Program: ConversionProg
         The program uses functions to convert between Binary, Hexadecimal and Decimal
"""
def DecToBin(Qot):
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



def BinToDec(Bin):
#   Bin = input("Enter a binary number: ")
    count = len(Bin)
    Dec = 0

    for digit in Bin:
        Dec += int(digit) * 2 ** (count - 1)
        count -= 1

    print(f"The Decimal equivalent of {Bin} is {Dec}")


def HexToBinary(Number):
    #print("\n\n\tHexadecimal Numbers contain digits and any letter from A to F\n")

    HexToBinary = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101',
                       '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
                       'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111', 'a':'1010', 'b':'1011',
                       'c':'1100', 'd':'1101', 'e':'1110', 'f':'1111'}
    Bin = []
    #Number = input("Please, Enter any Hexadecimal Number: ")
    for digit in Number:

        Bin.append(HexToBinary[digit]) 

    HexBinary = ''.join(map(str, Bin)) 

    print(HexBinary)

##########################################################################################################

print("\t WELCOME TO OUR CONVERSION PROGRAM\number")
print("\t\t - Press 1 to convert a Binary number to Decimal\n")
print("\t\t - Press 2 to convert an Hexadecimal number to Binary")
print("\t\t - Press 3 to convert a Decimal number to Binary")
Entry = int(input("\n\n\tChoose an option:   "))
if Entry == 1:
   print("\n\n\tBinary Numbers contain digits of 1 and 0\n")
   Bin = input("Enter a binary number: ")
   BinToDec(Bin)
elif Entry == 2:
    Qot = input("Please, Enter any Decimal Number: ")
    DecToBin(Qot)
elif Entry == 3:
    print("\n\n\tHexadecimal Numbers contain digits and any letter from A to F\n")
    Number = input("Please, Enter any Hexadecimal Number: ")
    HexToBinary(Number)
else:
    print("\n\nWE ARE STILL WORKING ON THE PROGRAM")

