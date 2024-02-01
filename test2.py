def v(n):
    n = str(n)
    res = n + int(n * 2) + int(n * 3)
    return res
n = int(input("Введіть ціле число n "))
res = v(n)
print(f"Вираз {n} + {n}{n} + {n}{n}{n} = {res}.")