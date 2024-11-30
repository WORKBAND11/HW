import math
a = float(input("Введите длину первого катета:" ))
b = float(input("Введите длину второго катета:" ))
x = a ** 2 + b ** 2
y = math.sqrt(x)
print("Гипотенуза:", y)
