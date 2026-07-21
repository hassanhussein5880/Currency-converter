print ("CURRENCY CONVERTER")
print ("USD to SAR")
print ("Quit")
rate = 3.76

option = int (input ("Pick option: "))
if option == 1:
    amount = int (input ("Amount in USD: "))
    total_result = amount * rate
    print (f"Result: {total_result} SAR")
else:
    print ("Quit")

