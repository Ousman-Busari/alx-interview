#!/usr/bin/env python3
"""
N queens
"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

n = int(sys.argv[1])
if n < 4:
    print("N must be at least 4")
    exit(1)


def moves(n, col=0, a=[], b=[], c=[]):
    """Checks possible movement and positions for the queen"""
    if col < n:
        for j in range(n):
            if j not in a and col + j not in b and col - j not in c:
                yield from moves(n, col + 1, a + [j],
                                 b + [col + j], c + [col - j])
    else:
        yield a


def solution(n):
    """Solutions"""
    positions = []
    col = 0
    for move in moves(n, 0):
        for s in move:
            positions.append([col, s])
            col += 1
        print(positions)
        positions = []
        col = 0


solution(n)
