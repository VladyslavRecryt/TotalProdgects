n = int(input("Введіть число n: "))

print(f"Парні числа від 1 до {n} у зворотному порядку:")
for i in range(n, 0, -1):
    if i % 2 == 0:
        print(i, end=" ")
