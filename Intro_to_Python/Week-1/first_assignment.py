first_input = input("Insert the first Number, ")
num1 = float(first_input)
second_input = input("Insert the second Number, ")
num2 = float(second_input)
operation = input("use + for Addition, - for subtraction, * for multiplication, / for division,  ")

if operation == '+':
    add = num1 + num2
    print('num1 + num2 = ',add)
elif operation == '-':
    sub = num1 - num2
    print('num1 - num2 = ',sub)
elif operation == '*':
    multi = num1 * num2
    print('num1 * num2 = ',multi)
elif operation == '/':
    division = num1 / num2
    print('num1 / num2 = ',division)
else:
    print("Please Insert correct data!")

