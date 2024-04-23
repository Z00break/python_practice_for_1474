name = input("name ")

f = open(r".\data.txt")
content = f.read()
f.close()


content = content.split()
y = open("data2.txt", "w")
y.write(" ".join(content))
y.close()


print(content)
if name in content:
    print(content.index(name)+ 1)
else:
    print(-1)

# print(type(content))
