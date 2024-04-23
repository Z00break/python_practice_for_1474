def divider2(slovo1, slovo2):
    try:
        return slovo1 / slovo2
    # except ZeroDivisionError:
    #     return -1 
    # except TypeError:
    #     return -1
    except (slovo1, slovo2):
        return -1


def summator(slovo1, slovo2):
    try:
        result = slovo1 + slovo2
    except TypeError:
        return slovo1 * slovo2

    # if type(result) == int:
    if isinstance(result, int):
        return ""
    return result
        

        
    # finally:
    #     print("function is done")    





# DRY


assert summator("abc", 3) == "abcabcabc"
assert summator(2, "kekw") == "kekwkekw"
assert summator("lol", "kek") == "lolkek"
assert summator(2, 4) == ""