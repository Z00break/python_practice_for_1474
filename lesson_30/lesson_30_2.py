from datetime import datetime as dt


# 1)создать дату (обьект datetime)
d1 = dt(2023, 10,26)
s1 = "2023, 10, 26"
d2 = dt.strptime(s1, "%Y, %m, %d")
assert d1 == d2

# 2)чтение даты

print(d2.day)
s2 = d2.strftime("%Y/%m/%d")
print(s2)

# 3)редактирование даты

# редактирование не возможно
