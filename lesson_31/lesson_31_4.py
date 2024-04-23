import sys


# print(sys.argv)
# if len(sys.argv) > 1:
#     num = int(sys.argv[1])
#     print(num * 10)


def foo(nums: list[int]) -> int| None:
    if len(nums) == 1:
        return None
    if nums[1] == "-add":
        return sum(map(int, nums[2:]))

# нечего переделывать в map


print(foo(sys.argv))
