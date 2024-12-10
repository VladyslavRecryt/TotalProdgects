points = int(input("Введіть кількість балів (0-100): "))

if 0 <= points <= 49:
    marks = "незадовільно"
elif 50 <= points <= 69:
    marks = "задовільно"
elif 70 <= points <= 89:
    marks = "добре"
elif 90 <= points <= 100:
    marks = "відмінно"
else:
    marks = "Некоректні бали!"

print(f"Рівень знань: {marks}")
