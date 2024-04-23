numbers = list(range(1,11))


def even_numbers(nums):
    return [number for number in nums if number % 2 == 0 ]
    # smun = []
    # for number in nums: 
    #     if number % 2 == 0:   
    #         smun.append(number)
    # return smun 



print(even_numbers(numbers))
print(even_numbers([1, 2, 3, 4]))
        

     