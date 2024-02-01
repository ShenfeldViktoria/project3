def V(lst):
    res = 1
    for i in lst:
        res *= i
    return res
l = [6, 3, 4, 5]
res = V(l)
print(f"Добуток елементів у списку {l} дорівнює {res}")