a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

temp = a
a = b
b = c
c = temp
print("After swapping:")
print("First number:", a)
print("Second number:", b)
print("Third number:", c)
