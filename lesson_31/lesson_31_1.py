from random import  randint, random, shuffle, choice, choices
import sys


def get_random_numbers(x: int) -> list[int]:
    return choices(list(range(1,101)), k=x)


# if len()) == 0:
#     print("Вы")
if len(sys.argv) == 1:
    print("ведите число")
if len(sys.argv) == 2:
    print(get_random_numbers(int(sys.argv[1])))
# x = randint(20, 30)
# print(x)

# x2 = random()
# print(x2)

# sp = list(range(1, 21))
# shuffle(sp)
# print(sp)

# x3 = choice(sp)
# print(x3)

# x4 = choices(sp, k = 5)
# print(x4)