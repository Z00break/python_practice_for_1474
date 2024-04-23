 # n = list(range(1,101))
# n2 = [el for el in n if el % 4 == 0 ] 
# print(n2)

n = list(range(1,21))
n2 = [el * 3  for el in n if el % 3 == 0 ]
# print(n2)

m = list("ABCD")
m2 = [(el, i * 100) for i, el in enumerate(m, start = 1)]
print(m2)
print(dict(m2))