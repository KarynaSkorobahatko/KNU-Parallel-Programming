import time
from math import gcd


def norm(num1, num2):
    return gcd(num1, num2) == 1


def normalize(chunk, input_list):
    start = time.time()
    res = []
    for number in chunk:
        for s_number in input_list:
            if norm(number, s_number):
                if number > s_number:
                    res.extend([number, s_number])
                else:
                    res.extend([s_number, number])
    return time.time() - start, res