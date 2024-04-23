#name = input()

####if "a" in name:
####    print(len(name))
####else:
####    print("в имени нет буквы а")




numbers = [3, 1, 5, 0]

if 4 in numbers:
    numbers.append(6)
elif 3 in numbers:
    numbers.append(0)
else:
    numbers.append(5)

print(numbers)
