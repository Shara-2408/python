x = input("Enter the marital status: ").strip().lower()
y = input("Enter the gender: ").strip().lower()
z = int(input("Enter the Age: "))

if x == "married":
    print("Driver insures")
elif x == "unmarried" and y == "male" and z > 30:
    print("Insures")
elif x == "unmarried" and y == "female" and z < 25:
    print("Insures")
else:
    print("Will not insure")
