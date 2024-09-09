def decimal_to_binary(decimal_number):
    return bin(decimal_number)[2:] 


decimal_number=input("Enter a decimal_number: ")
print(f"Decimal: {decimal_number}, octal: {decimal_to_binary(decimal_number)}")
