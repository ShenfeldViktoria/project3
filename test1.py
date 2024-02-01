import math
def P():
    rad = input("Введіть радіус кола ")
    try:
        r = float(rad)
        area = math.pi * r**2
        print(f"Площа кола  радіусом {r} дорівнює {area} см ^2")
    except ValueError:
        print("Введіть коректне значення для радіусу")
P()