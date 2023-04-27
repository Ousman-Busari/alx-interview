#!/usr/bin/python3
""" Module for Pascal's triangle """


def pascal_triangle(n):
    """ Returns list of lists of ints representing Pascal's triangle of n """

    if n <= 0:
        return []

    """ initialize an empty resulting array """
    triangle = [[] for idx in range(n)]

    for row in range(n):
        for col in range(row + 1):
            if(col < row):
                if(col == 0):
                    """ the first column is always set to 1 """
                    triangle[row].append(1)
                else:
                    triangle[row].append(triangle[row-1][col - 1] + triangle[row-1][col])
            elif(col == row):
                """ the diagonal is always set to 1 """
                triangle[row].append(1)

    return triangle
