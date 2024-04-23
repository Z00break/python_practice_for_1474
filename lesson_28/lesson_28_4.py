b = [1, 2, 3., 'A', 'B', 5]
# b = [1, 2, 3.]
# b = ['a', 'b', 'c']
len_before = len(b)
for i in range(len(b) - 1, -1, -1):
    if isinstance(b[i], str):
    # if type(b[i]) is str:
    #     b.remove(b[i])
        del b[i]

assert len_before > len(b), " не проверенно :( , длина не изменилась"

print(b)


raise ValueError