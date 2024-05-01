import calculator_functions as calc
import os

print("##########################################################")
print("This is a Calculator developed by Alexandre D. Caspechaque")
print("##########################################################\n")

active = True
firstRun = True

while active:
    if not firstRun:
        num1 = result
        print(num1)
        operator = input()
        num2 = input()

        if num2 == "exit" or num2 == "exit":
            active = False
            break

    if firstRun:
        num1 = input("num1: ")
        operator = input("operator: ")
        num2 = input("num2: ")
        firstRun = False

    if operator == "+":
        result = calc.sum(num1, num2)
        os.system("cls")
    elif operator == "-":
        result = calc.sub(num1, num2)
        os.system("cls")
    elif operator == "/":
        result = calc.div(num1, num2)
        os.system("cls")
    elif operator == "*":
        result = calc.mul(num1, num2)
        os.system("cls")
