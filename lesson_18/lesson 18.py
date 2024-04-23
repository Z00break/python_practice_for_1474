f = open("data.txt")
content = f.read()
# content2 = f.readlines()
f.close()
print(repr(content))
print(content.split())
# print(content2)

with open("data2.txt", "w") as file:
    content = content.split()
    file.write(" ".join(content))