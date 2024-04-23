# # y = input("выбирете число 3,6,10,15,21,28 :")

# stars = [ "*" * 7,"*" * 6,"*" * 5,"*" * 4,"*" * 3,"*" * 2,"*" * 1 ]

# .

# print(stars)

# n = вводим()

# шаг = 1

# пока n > 0:
#     печатаем(шаг)
#     n = n - шаг
#     шаг += 1


# n = input()
# n = int(n)
# step = 1

# while n > 0:
#     print(step)
#     n = n - step
#     step += 1

sp = []
n = int(input())


shag = 1

while n > 0:
    sp.append(shag)
    n = n - shag
    shag = shag + 1
sp.reverse() 
for d in sp:
    print(d * "*")

  