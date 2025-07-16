max = 5
total = 0.0
print("This program calculates thee sum of")
print(max,"number you will enter. ")
for counter in range(max):
    number = int(input("Enter  a number: "))
    total = total + number
print("THe total is",total)