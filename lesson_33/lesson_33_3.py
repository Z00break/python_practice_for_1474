i = [7, 10, 21, 26]
l = 303


for u in i:
    if u > l:
        i.insert(i.index(u), l)
        break
else:
    i.append(l)


print(i)