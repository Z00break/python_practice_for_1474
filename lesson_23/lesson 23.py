# 1)надо написать функцию которая делит число на число 


def devider(number1, number2 = 2):
    f = number1 / number2
    return f

result = devider(10, number2=5)
assert result == 5.0 
assert result < 6