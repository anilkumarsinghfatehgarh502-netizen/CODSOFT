# simple calculator
    # two number are N1 and N2
N1=float(input("Enter first number:"))
N2=float(input("Enter second number:"))
print("choose an operation:")
print("+. Addition")
print("-. Subtraction")
print("*. Multiplication")
print("/. Division")
choice = input("Enter your operation(+,-,*,/):")

# perform operation based on your operation
if choice == '+':
    result = N1 + N2
    print("Result:", result)
elif choice == '-':
    result = N1 - N2
    print("Result:", result)
elif choice == '*':
    result = N1 * N2
    print("Result:", result)
elif choice == '/':
    if N2 != 0:
        result = N1 / N2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("You Choose wrong Operation")


        
