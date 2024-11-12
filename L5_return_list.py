
def return_list_of_numbers_inbetween(a, b):
    aol = []
    keep_going = True
    current_number = a
    while keep_going:
        aol.append(current_number)
        current_number += 1
        if current_number == b + 1:
            keep_going = False
    return aol

n1 = input("give me a number")
n1 = int(n1)

n2 = input("a second number")
n2 = int(n2)

all_numbers = return_list_of_numbers_inbetween(n1, n2)
print(n1, n2, all_numbers)