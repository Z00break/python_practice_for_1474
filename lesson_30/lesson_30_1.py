from time import sleep, time


# sleep(5)
# print("pasha")
def hello(name: str) -> None:
    """

    :param name:
    :return:
    """

    sleep(2)
    print(name)
    sleep(2)
    print("конец")


start: float = time()
hello("паша")
print(time() - start)