def v(lst):
    if not lst:
        return None 
    min = lst[0]
    for i in lst:
        if i < min:
            min = i
    return min
l = [10, 2, 8, 1, 5]
res = v(l)
print(f"Найменше число у списку {l} - це {res}.")
