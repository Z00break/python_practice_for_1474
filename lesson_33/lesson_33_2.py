
def sort_numbers(u):
    with open(u, "r") as file:
        content = file.read().split()
    r = []
    # content = file_data.read().split()

    for i in content:
        i = int(i)
        if len(r) == 0:
            r.append(i)
        else:
            for j in r:
                if i < j:
                    r.insert(r.index(j), i)
                    break
            else:
                r.append(i)
    # file_data.close()

    new_file = open(u, "w")

    for t in r:
        new_file.write(str(t) + "\n")

    new_file.close()
    return r


print(sort_numbers("numbers.txt"))