import math

from lab2_module import def_number  # Імпорт функції з модуля

# Функція для обчислення значення виразу z
def calculate_z(x):
    return (math.sqrt(2) / 2) * math.sin(1 / x) + 1

# Основна програма
x = float(input("Введіть значення x: "))
z = calculate_z(x)
print(f"Значення z: {z}")

n = int(input("Введіть число n: "))
if def_number(n):
    print(f"Число {n} є недостатнім.")
else:
    print(f"Число {n} не є недостатнім.")
