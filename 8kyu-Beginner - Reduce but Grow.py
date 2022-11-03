

# DESCRIPTION:
# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

# FUNDAMENTALSARRAYS


def grow(arr):
    grow=1
    for item in arr:
        grow*=item
    return grow

