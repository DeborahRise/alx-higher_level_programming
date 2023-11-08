#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    score = weight = 0
    for tup in my_list:
        score += (tup[0] * tup[1])
        weight += (tup[1])
    return (score / weight)
