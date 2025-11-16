# 05_input_and_type_casting.py
# Concept: input(), int(), float(), type casting

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

print("Before casting:", type(num1), type(num2))

num1 = float(num1)
num2 = float(num2)

print("After casting:", type(num1), type(num2))
print("Sum =", num1 + num2)
