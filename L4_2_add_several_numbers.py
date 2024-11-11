
def add_several_numbers():
    total = 0
    want_more = True
    while want_more:
        s=input("please write a number or to stop write stop:")
        if s == "stop":
            want_more = False
        else:
            # add this to what the number currently is
            n=int(s)
            total =total+n



    return total

total = add_several_numbers()
print(total)