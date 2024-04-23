import sys


# def one_change(n: int) -> None:
#     b = ["0" * n] * n
#     for si, s in enumerate(b):
#         s = list(s)
#         s[si] = "X"
#         s = "".join(s)
#         print(s)
#
#
#
#
# one_change()
args = sys.argv
# if len(args) in (1,2):
# if 1 <= len(args) <= 2:
# if len(args) == 2 or len(args) == 1:
if len(args) == 2:
    print(args[1])
elif len(args) == 1:
    pass
else:
    print(int(args[1]) + int(args[2]))
