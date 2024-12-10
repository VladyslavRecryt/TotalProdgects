import random

number = random.randint(1, 10)
sprob = 3

print('Я бот дуже розумний і знаю тільки 10 цифр, тому вгадай число від 1 до 10')

for attempt in range(1, sprob + 1):
    vgadai = int(input(f"Спроба {attempt}: Введіть ваше число: "))

    if vgadai == number:
        print("Вітаю! Ви вгадали число!")
        break
    elif vgadai > number:
        print("Менше.")
    else:
        print("Більше.")
else:
    print(f"На жаль, ви програли. Загадане число було: {number}.")
