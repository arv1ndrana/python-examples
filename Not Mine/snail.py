"""
        Snail Sort

        Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

        array = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]

        snail(array) #=> [1,2,3,6,9,8,7,4,5]
"""


def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1]  # Rotate
    return out
