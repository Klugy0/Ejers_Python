def sumar_todos(*args):
    if not args:
        return 0
    total = sum(args)
    return total

print(sumar_todos(1, 2, 3)) # ➜ 6
print(sumar_todos(10, 20, 30, 40))  # ➜ 100
print(sumar_todos())# ➜ 0
