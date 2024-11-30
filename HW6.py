import math
b = float(input("Введите основание логарифма:" ))
x = float(input("Введите число:" ))
c = math.log(x)
d = math.log(x, b)
e = math.log10(x)
print(f"Натуральный логарифм:", c)
print("Логарифм по оснаванию", b, x)
print(f"Десятичный логарифм:", x)