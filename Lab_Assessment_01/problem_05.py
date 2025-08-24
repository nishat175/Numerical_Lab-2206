operator = input("Input an operator(+,-,*,/): ")

n1 = int(input("Input the first number: "))
n2 = int(input("Input the second number: "))

if operator == "+":
    print(f"{n1}+{n2} = {n1+n2}")
elif operator == "-":
    print(f"{n1}-{n2} = {n1-n2}")
elif operator == "*":
    print(f"{n1}*{n2} = {n1*n2}")
elif operator == "/":
    if n2 != 0:
        print(f"{n1} / {n2} = {n1/n2:.2f}")
    else:
        print("Error! Division by zero")
else:
    print("Invalid operator")