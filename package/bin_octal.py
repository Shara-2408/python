def binary_to_octal(binary_number):
    return int(binary_number,2)
binary_number=input("Enter a binary_number: ")
print(f"Binary={binary_number},octal:{binary_to_octal(binary_number)}")