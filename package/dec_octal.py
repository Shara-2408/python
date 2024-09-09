def decimal_to_octal(decimal_number):
    return oct(decimal_number)[2:] 

decimal_number=input("Enter a decimal_number: ")
print(f"Decimal: {decimal_number}, octal: {decimal_to_octal(decimal_number)}")