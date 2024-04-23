


def create_list(value: str, amount: int) -> list[str]:
    """
    создает список из символа велью каличество амаунт
    :param: value
    :param: amount
    :return: 
    """
    return [ value for a  in range(amount )]

# print(create_list("y", 3))
print(create_list(0, 2))