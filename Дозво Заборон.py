name = input("Введіть ваше ім'я: ")
age = int(input("Введіть ваш вік: "))
if age < 18:
    print('Вхід Заборонино')
else:
    print('Вхід Дозволено')
print(f"Привіт {name}, тобі {age}!")