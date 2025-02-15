import random
import maths

def mutate(a_list):
    b_list = []
    new = []
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new.append(maths.add(new_item, item))
    b_list.append(new)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
