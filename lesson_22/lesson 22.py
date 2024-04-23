
# список, среди всех цихр есть одна которая не повторяеться - все кроме неё повторяются два раза
numbers = [1, 2, 1, 2, 3, 4, 4]
# numbers = []
# надо написать функцию которая принимает такой список и возвращает это цифра


def find_unique(nums):
    seen = []
    for number in nums:
        if number in seen:
            seen.remove(number)
        else:
            seen.append(number)
    # try:
    #     return seen[0]
    # except IndexError:
    #     return None

    # if len(seen) == 0:
    #     return None
    # else:
    #     return seen[0]

    return seen[0] if seen else None


print(find_unique(numbers))
print(find_unique([]))
assert find_unique(numbers) == 3
