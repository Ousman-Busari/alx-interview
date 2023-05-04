#!/usr/bin/python3
"""
0-minoperations
"""


def minOperations(n):
    """
    In a text file, there is a single character H. Your text editor
    can executeonly two operations in this file: Copy All and Paste.
    Given a number n, this a method calculates the fewest number of
    operations needed to result in exactly n H characters in the file.
    """

    operations = 0
    if n <= 1 or type(n) is not int:
        return 0

    for i in range(2, n + 1):
        """
        check if i is a factor of n
        """
        while n % i == 0:

            """
            if i is a factor of n, break n into smaller
            parts to find the highest possible factor of
            n which i it's multiple
            """
            n = n / i

            """
            then sum up all the number of smaller parts
            (paste smaller parts number of factor 'i' times)
            """
            operations += i
    return operations
