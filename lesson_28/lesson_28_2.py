n = list(range(1, 21))
n2 = list(range(1, 21))
d = []
for number in n:
    if number % 4 == 0:
        n.remove(number)

print(n)

del n2[3::4]
print(n2)