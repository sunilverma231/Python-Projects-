num_1 = float(input("Enter the first number: "))
ope = input("Enter the operator: ")
num_2 = float(input("Enter the second number: "))
if ope == "+":
    print(num_1 + num_2)
elif ope == "-":
    print(num_1 - num_2 )
elif ope == "*":
    print(num_1 * num_2)
elif ope == "/":
    print(num_1 / num_2)
else:
    print("Invalid operator")

