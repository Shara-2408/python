def decimal_to_hex(decimal_number):
    return hex(decimal_number)[2:]

decimal_number=input("Enter a decimal_number: ")
print(f"Decimal: {decimal_number}, Hexadecimal: {decimal_to_hex(decimal_number)}")