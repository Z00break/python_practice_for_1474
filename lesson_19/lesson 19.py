x = 5
name = "pasha\n"
# f = open(r"C:\Users\Павел\Downloads\lessons\lesson_19\data.txt", "a")
f = open("data.txt", "a")

for i in range(x):
    f.write(name)
f.close()