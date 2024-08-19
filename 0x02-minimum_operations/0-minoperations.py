#!/usr/bin/python3

"""Method that determines the number of minmum operations given n characters"""

def minOperations(n):
    """A function that calculates the fewest number of operations"""

    result = 0
    x = 2
    while n > 1:
        while n % x == 0:
            result += x
            n /= x
        x += 1
    return result