import math
result = 0.0
total = 0.0
num_calc = 0
cond = True
print("Current Result:", result)
print("Calculator Menu")
print("---------------")
listy = ["Exit Program", "Addition", "Subtraction", "Multiplication", "Division", "Exponentiation", "Logarithm", "Display Average"]
for i in range(0,8):
    print(str(i)+". " + listy[i])
op = int(input("Enter Menu Selection: "))
while cond:
    if op == 0:
        print("Thanks for using this calculator. Goodbye!")
        cond = False
    elif op == 1:
        num1 = float(input("Enter first operand: "))
        num2 = float(input("Enter second operand: "))
        result = num1+num2
        total += result
        num_calc+=1
        print("Current Result: ", result)
        print("Calculator Menu")
        print("---------------")
        for i in range(0, 8):
            print(str(i) + ". " + listy[i])
        op = int(input("Enter Menu Selection: "))
    elif op == 2:
        num1 = float(input("Enter first operand: "))
        num2 = float(input("Enter second operand: "))
        result = num1 - num2
        total += result
        num_calc+=1
        print("Current Result: ", result)
        print("Calculator Menu")
        print("---------------")
        for i in range(0, 8):
            print(str(i) + ". " + listy[i])
        op = int(input("Enter Menu Selection: "))
    elif op == 3:
        num1 = float(input("Enter first operand: "))
        num2 = float(input("Enter second operand: "))
        result = num1 * num2
        total += result
        num_calc+=1
        print("Current Result: ", result)
        print("Calculator Menu")
        print("---------------")
        for i in range(0, 8):
            print(str(i) + ". " + listy[i])
        op = int(input("Enter Menu Selection: "))
    elif op == 4:
        num1 = float(input("Enter first operand: "))
        num2 = float(input("Enter second operand: "))
        result = num1 / num2
        total += result
        num_calc+=1
        print("Current Result: ", result)
        print("Calculator Menu")
        print("---------------")
        for i in range(0, 8):
            print(str(i) + ". " + listy[i])
        op = int(input("Enter Menu Selection: "))
    elif op == 5:
        num1 = float(input("Enter first operand: "))
        num2 = float(input("Enter second operand: "))
        result = num1 ** num2
        total += result
        num_calc+=1
        print("Current Result: ", result)
        print("Calculator Menu")
        print("---------------")
        for i in range(0, 8):
            print(str(i) + ". " + listy[i])
        op = int(input("Enter Menu Selection: "))
    elif op == 6:
        num1 = float(input("Enter first operand: "))
        num2 = float(input("Enter second operand: "))
        result = math.log(num2, num1)
        total += result
        num_calc+=1
        print("Current Result: ", result)
        print("Calculator Menu")
        print("---------------")
        for i in range(0, 8):
            print(str(i) + ". " + listy[i])
        op = int(input("Enter Menu Selection: "))
    elif op == 7:
        if num_calc != 0:
            print("Sum of calculations:", total)
            print("Number of calculations:", num_calc)
            print("Average of calculations:", round((total / num_calc), 2))
            op = int(input("Enter Menu Selection: "))
        else:
            print("Error: No calculations yet to average!")
            op = int(input("Enter Menu Selection: "))
    else:
        print("Error: Invalid selection!")
        op = int(input("Enter Menu Selection: "))

