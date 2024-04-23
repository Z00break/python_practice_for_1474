

def arguments(v, *args, x=2, **kwargs):
    # q = str(v)+"-"
    q = f"{v}-"
    for i in args:
    #    q = q + str(i) + "-"
       q += f"{i}-"

    # q = q + "x-" + str(x) + "-" 
    q += f"x-{x}-"   

    for y in kwargs:
        # q = q + y + "-" + str(kwargs[y]) + "-"
        q += f"y-{kwargs[y]}-"
    
    q = q[: -1]
    return q


    # print(v, args, x, kwargs, w)


print(arguments(2, 34, 23, 56, x=3, t=4, r=6))   


# arguments(10, 15, 20, 25, x=1, a=2, b=3)

# 10-15-20-25-x-1-a-2-b-3


# arguments(2, 34, 23, 56, x=3, t=4, r=6)

# 2-34-23-56-x-3-t-4-r-6