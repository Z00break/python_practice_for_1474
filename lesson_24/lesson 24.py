def my_maths(x, y=2, z=4):
    return x * y / z


# print(my_maths(4, z=10, y=20))

assert my_maths(8) == 4


def my_sum(*args):
    return sum(args)
    # print(nums)


print(my_sum(1)) 

# my_sum([1, 2, 3])

print(my_sum(1, 2, 6))


def my_kwargs(**kwargs):
    print(kwargs)


my_kwargs()

my_kwargs(a=2)

my_kwargs(e = 87)