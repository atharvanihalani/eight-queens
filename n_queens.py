from typing import List
import numpy as np
from math import cos, sin, pi
import math
import copy

# for n > 3



cons = {}
ans = []

def populate_constraints(n: int):
    for i in range(n):
        cons[i] = constraints_at(i, n)

def constraints_at(row: int, n: int) -> List[List[int]]:
    all_cols = []

    for i in range(1, n):
        col = [1, 1, 1, 1, 1, 1, 1, 1]
        col[row] = 0
        if row - i >= 0:
            col[row - i] = 0 
        if row + i < n:
            col[row + i] = 0
        all_cols.append(col)
    
    return all_cols

def backtrackin(col: int, state: List[List[int]], stack: List, n: int):
    for i in range(n):
        if col != 1 and state[col-2][i] == 0:
            continue
        
        backtrack = False
        temp_state = copy.deepcopy(state)
        for j in range(n-col):
            for x in range(n):
                if cons[i][j][x] == 1 and state[col-1 + j][x] == 1:
                    temp_state[col-1 + j][x] = 1
                else:
                    temp_state[col-1 + j][x] = 0

        zero = [0] * n
        if zero in temp_state:
            continue

        temp_stack = copy.deepcopy(stack)
        temp_stack.append((col, i+1))

        if col == n-1:
            global ans
            ans.append(temp_stack)
            print(temp_stack)
        else:
            backtrackin(col + 1, temp_state, temp_stack, n)

def solution(n: int):
    populate_constraints(n)
    state = [[1 for _ in range(n)] for __ in range(n-1)]
    backtrackin(1, state, [], n)


def parse_sols(sols: List[List[tuple]]):
    # while 
    # returns the unique solutions
    pass

def gen_variants(sol: List[tuple], n: int) -> List[List[tuple]]:
    variants = []

    variants.append([(x[0], n+1-x[1]) for x in sol])
    for i in range(3):
        sol = rotate(sol, n)
        variants.append(sol)
        variants.append([(x[0], n+1-x[1]) for x in sol])

    return variants

def rotate(sol: List[tuple], n: int) -> List[tuple]:
    # rotates the chessboard by 90°
    copy_sol = copy.deepcopy(sol)
    for i in range(len(copy_sol)):
        if n % 2:
            # normalizes 
            x = copy_sol[i][1] - math.ceil(n/2)
            y = -copy_sol[i][0] + math.ceil(n/2) 
            # rotates 90° clockwise
            copy_sol[i] = (y, -x)

            # un-normalizes
            x_ = -copy_sol[i][1] + math.ceil(n/2)
            y_ = copy_sol[i][0] + math.ceil(n/2)
            copy_sol[i] = (x_, y_)
        else:
            x = copy_sol[i][1] - (n/2 + 1) if copy_sol[i][1] <= n/2 else copy_sol[i][1] - n/2
            y = -copy_sol[i][0] + (n/2 + 1) if copy_sol[i][0] <= n/2 else -copy_sol[i][0] + n/2
            copy_sol[i] = (y, -x)

            x_ = -copy_sol[i][1] + (n/2 + 1) if copy_sol[i][1] > 0 else -copy_sol[i][1] + n/2
            y_ = copy_sol[i][0] + (n/2 + 1) if copy_sol[i][0] < 0 else copy_sol[i][0] + n/2
            copy_sol[i] = (x_, y_)
    return copy_sol



# solution(4)
# print(len(ans))
