name = input()

if len(name) > 15:
    print("большое")
elif len(name) > 6:
    print("среднее")
else:
    print("маленькое")
