from lab2_module import def_number  # Імпорт функції з модуля

n = int(input("Введіть число n: "))
if def_number(n):
    print(f"Число {n} є недостатнім.")
else:
    print(f"Число {n} не є недостатнім.")
