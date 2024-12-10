a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
rahyvana = input(" дія (+, -, *, /): ")

if rahyvana == "+":
    result = a + b
elif rahyvana == "-":
    result = a - b
elif rahyvana == "*":
    result = a * b
elif rahyvana == "/":
     result = a / b
else:
    result = "Некоректна дія!"

print(f"Результат: {result}")
