


def one_change(n: int) -> None:
    b = ["0" * n] * n
    for si, s in enumerate(b):
        s = list(s)
        s[si] = "X"
        s = "".join(s)
        print(s)




one_change(5)





