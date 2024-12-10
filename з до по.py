start = int(input("Введіть число 'з': "))
end = int(input("Введіть число 'по': "))

print(f"Числа від {start} до {end}:")
for i in range(start, end + 1):
    print(i, end=" ")
