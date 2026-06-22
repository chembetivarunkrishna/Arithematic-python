# Python Program Demonstrating All Operators

# 1. Arithmetic Operators
print("=== Arithmetic Operators ===")
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))

area = length * width
perimeter = 2 * (length + width)

print("Area =", area)
print("Perimeter =", perimeter)

# 2. Comparison Operators
print("\n=== Comparison Operators ===")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is less than", num2)
else:
    print("Both numbers are equal")

# 3. Logical Operators
print("\n=== Logical Operators ===")
num = int(input("Enter a number: "))

if num >= 10 and num <= 50:
    print("Number is within the range 10 to 50")
else:
    print("Number is outside the range")

text = input("Enter a string: ")

if text == "Python" or text == "python":
    print("String matches Python")
else:
    print("String does not match Python")

# 4. Assignment and Augmented Assignment Operators
print("\n=== Assignment Operators ===")
x = 10
print("Initial Value:", x)

x += 5
print("After += 5:", x)

x -= 3
print("After -= 3:", x)

x *= 2
print("After *= 2:", x)

x /= 4
print("After /= 4:", x)

x %= 3
print("After %= 3:", x)

x **= 2
print("After **= 2:", x)

# 5. Identity and Membership Operators
print("\n=== Identity and Membership Operators ===")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2:", list1 is list2)
print("list1 is not list3:", list1 is not list3)

print("2 in list1:", 2 in list1)
print("5 not in list1:", 5 not in list1)

word = "Python"
print("'P' in word:", 'P' in word)
print("'z' not in word:", 'z' not in word)