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

    total_H = 1  # total number of H present in the text file
    memory = 0  # number of H copied to the clipboard
    operations = 0  # keeps count of the number of operations

    # while the total number of H present is less then n
    while total_H < n:
        # if nothing isnnot yet copied to memory
        if memory == 0:
            # copy the total number of char
            memory = total_H
            # then paste it back to
            total_H += memory
            # with the above copy and paste, increase operations by 2
            operations += 2
            # then continue from the next loop
            continue

        remaining_H = n - total_H
        # if number of H copied to the memory is more
        # than the number required, then n is impossible
        # to achive
        if remaining_H < memory:
            return 0

        # if total H is a factor of remaining_H
        if remaining_H % total_H == 0:
            # then copy total_H to memory
            memory = total_H
            # then paste it to the etx file
            total_H += memory
            # with the above copy and paste, increase operations by 2
            operations += 2
        # if total_H is not a factor of remianing_H
        else:
            # paste the memory H to the text file
            total_H += memory
            # then increase operations count by 1
            operations += 1

    return operations
