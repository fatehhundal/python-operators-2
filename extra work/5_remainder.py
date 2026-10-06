num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

fin_num = int(num1 / num2)
remainder = num1 % num2
print(num1, "÷", num2, "=", fin_num, "(nearest whole number)")
print("Remainder:", remainder)