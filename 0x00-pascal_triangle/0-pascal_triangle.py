#!/usr/bin/python3

def pascal_triangle(n):
    """returns a list of lists of intergers representing
    Pascal's triangle"""
    if n <= 0:
        return []
    if n == 1:
        return [1]
    triangle = [pascal_triangle(1)]
    for i in range(n - 1):
        row = [1]
        prev_row = triangle[len(triangle) - 1]
        for i in range(len(prev_row)):
            if i <= len(prev_row) - 2:
                row.append(prev_row[i] + prev_row[i + 1])
            else:
                row.append(1)
        triangle.append(row)
    return triangle