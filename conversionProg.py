"""
Djeme Doli 07/17/2023
Program: ConversionProg
         The program uses functions to convert between Binary, Hexadecimal and Decimal
"""
def DecToBin(Qot):
    if Qot.isdigit():
       Qot = int(Qot)
       Bin = []
       while Qot != 0:
             Mod = Qot % 2   # The modulo of any number by 2 is either 0 or 1
             Bin.insert(0, Mod)
             Qot = Qot // 2     
    else:
        print("You have not entered a Decimal")
        return
    DecBinary = "".join(map(str, Bin)) # Convert each element of the list to String, then join them all together
    return DecBinary 

def BinaryCheck(strg):
    isBinary = True
    for element in strg:
        if (element != '0') and (element != '1'):
           isBinary = False
           break
    return isBinary
        

def BinToDec(Bin):
#   Bin = input("Enter a BINARY number (0s and 1s only): ")    
    if len(Bin) != 0:
       Dec = 0
       count = len(Bin) 
       for digit in Bin:
         count -= 1
         Dec += int(digit) * (2 ** count)
       return Dec
    else:
        return None



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

###############

print("\t WELCOME TO OUR CONVERSION PROGRAM\n")
print("\t\t - Press 1 to convert a Binary number to Decimal\n")
print("\t\t - Press 2 to convert a Decimal number to Binary\n")
print("\t\t - Press 3 to convert an Hexadecimal number to Binary\n")

while True:
 Entry = input("\n\n\tChoose an option (Press Enter to exit): ")
 if Entry == '1':
   print("\n\n\tBinary Numbers contain digits of 1 and 0 only\n")
   while True:
         Bin = input("Enter a binary number / press Enter to exit: ")
         if BinaryCheck(Bin):
            print("The Decimal equivalent of ",Bin, "is: ",BinToDec(Bin))
         else:
             print("This is not a valid Binary number")
         if Bin == "":
            break
 elif Entry == '2':
    while True:
          Qot = input("Please, Enter any Decimal Number / press Enter to exit: ")
          if Qot == "":
             break
          else:
            print(DecToBin(Qot))
 elif Entry == '3':
    print("\n\n\tHexadecimal Numbers contain digits and any letter from A to F\n")
    Number = input("Please, Enter any Hexadecimal Number: ")
    HexToBinary(Number)
    
 elif Entry == "":
     break

