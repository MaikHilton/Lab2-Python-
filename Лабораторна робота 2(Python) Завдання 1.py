import math

# Функція для обчислення значення виразу z
def calculate_z(x):
    if x == 0:
        return "Помилка: ділення на нуль неможливе"
    return (math.sqrt(2) / 2) * math.sin(1 / x) + 1

# Функція для визначення, чи є число недостатнім
def def_number(n):
    divisors_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisors_sum < n

# Основна програма
x = float(input("Введіть значення x: "))
z = calculate_z(x)
print(f"Значення z: {z}")

n = int(input("Введіть число n: "))
if def_number(n):
    print(f"Число {n} є недостатнім.")
else:
    print(f"Число {n} не є недостатнім.")
