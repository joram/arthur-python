import random
from datetime import datetime


def return_number_between_1_and_10():
    n = random.choice([1,2,3,"hello arthur (; (:"])
    print(n)


start = datetime.now()
for i in range (1,99999999999999999999999999999999999999999999999999999999999):
    if i % 10000000 == 0:
        print(i)
    # return_number_between_1_and_10()
end = datetime.now()
diff = end - start
print(diff)