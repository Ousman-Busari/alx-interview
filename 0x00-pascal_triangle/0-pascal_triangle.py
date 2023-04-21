#!/usr/bin/python3
""" Module for Pascal's triangle """


def pascal_triangle(n):
    """ Returns list of lists of ints representing Pascal's triangle of n """

    if n <= 0:
        return []

    """ initialize an empty resulting array """
    pascal = [[] for idx in range(n)]

    for li in range(n):
        for col in range(li+1):
            if(col < li):
                if(col == 0):
                    """ the first column is always set to 1 """
                    pascal[li].append(1)
                else:
                    pascal[li].append(pascal[li-1][col] + pascal[li-1][col-1])
            elif(col == li):
                """ the diagonal is always set to 1 """
                pascal[li].append(1)

    return pascal

# #!/usr/bin/python3
# """
# Pascal Triangle
# """


# def pascal_triangle(n):
#     """Returns a list of lists of intergers representing
#     Pascal's triangle"""
#     if n <= 0:
#         return []
#     if n == 1:
#         return [1]
#     triangle = [pascal_triangle(1)]
#     for i in range(n - 1):
#         row = [1]
#         prev_row = triangle[len(triangle) - 1]
#         for i in range(len(prev_row)):
#             if i <= len(prev_row) - 2:
#                 row.append(prev_row[i] + prev_row[i + 1])
#             else:
#                 row.append(1)
#         triangle.append(row)

#     return triangle
