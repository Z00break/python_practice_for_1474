

def search_transition(x, y):
    i = 0
    while True:
        i = i + 1
        if x == y or x == 0:
            return None
        if x > y:
            x >>= 1
            if x < y:
                return None
            if x == y:
                return f">>{i}"
        elif x < y:
            x <<= 1
            if x > y:
                return None
            if x == y:
                # return "<<" + str(i)
                return f"<<{i}"




search_transition(100, 100)
search_transition(15, 40)
assert search_transition(16, 128) == "<<3"
assert search_transition(201, 6) == ">>5"
assert search_transition(1820584, 3) == ">>19"
assert search_transition(1, 0) == ">>1"
assert search_transition(100, 100) is None
assert search_transition(8, 5) is None

