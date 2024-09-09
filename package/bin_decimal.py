def binary_to_decimal(binary_number):
    return int(binary_number,2)
binary_number=input("Enter a binary_number: ")
print(f"Binary={binary_number},Decimal:{binary_to_decimal(binary_number)}")