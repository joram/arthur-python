a = "arthur" # string
b = 123    # integer
c = "123"  # string
d = 123.0  # float
e = ["arthur", "john", "ruby", "caitlin"]   # list




def return_list_of_numbers_inbetween(a, b):
    my_list = []
    my_list = ["arthur", "john", "ruby", "caitlin"]


    return my_list

n1 = input("give me a number")
n1 = int(n1)

n2 = input("a second number")
n2 = int(n2)

all_numbers = return_list_of_numbers_inbetween(n1, n2)
print(n1, n2, all_numbers)