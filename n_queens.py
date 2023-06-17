from typing import List
import math
import copy

'''
here's a tl;dr for how it all works:
first, i set up the constraints dict. this encodes the constraints
propagated by placing a queen at any particular square. 
then, i iterate: 
    placing a queen at (1, 1)
    applying its constraints
        placing a queen in the next column, at the next valid square
        ...and recursing
    if the constraints don't leave room in any future column, i move
    on to the next iteration
last, i parse the output to generate unique solutions
iterating through the solutions list:
    for each solution, i generate all its possible variants (through
    rotations and flips). 
    these variants are all pruned from sols
'''

'''
cons[i][j] tells you how placing a queen at the i'th row (for ANY column)
affects the constraints of the (j+1)'th column to its right. The key (lol) to 
deciphering this, is converting the integers to 8-bit strings. The 1's
represent open spots, while the 0's are squares under attack'''
cons = {}
sols = []

def solution(n: int):
    '''
    'top-level' method that generates solutions for an nxn board
    these are populated in the sols list
    n: n'''
    populate_constraints(n)
    state = [[1 for _ in range(n)] for __ in range(n-1)]
    backtrackin(1, state, [], n)

def populate_constraints(n: int):
    '''
    populates the entire constraints matrix \n
    n: side length of the board'''
    for i in range(n):
        cons[i] = constraints_at(i, n)

def constraints_at(row: int, n: int) -> List[List[int]]:
    '''
    calculates the constraints propagating outward from any
    cell in a particular row \n
    row: the index of the row
    n: length of the board'''
    all_cols = []

    for i in range(1, n):
        col = [1 for _ in range(n)]
        col[row] = 0
        if row - i >= 0:
            col[row - i] = 0 
        if row + i < n:
            col[row + i] = 0
        all_cols.append(col)
    
    return all_cols

def backtrackin(col: int, state: List[List[int]], stack: List, n: int):
    '''
    This method recursively backtracks through the various permutations.
    It's faster than an 8! brute force, only because it 'prunes' invalid perms early
    and efficiently.
    It places a queen in a valid square, applies constraints to the subsequent columns,
    and, if the constraints aren't 'too' constraining, it recurses (ie. tries to place a 
    queen in the next column). If however, the constraints leave no room for a queen in 
    a future col, it checks the next square in that column.

    col: the current column 
    state: the current state of all constraints. note len(state) = 7, because the first 
           column doesn't rlly have any constraints.
    stack: ie. the state of the board in the levels 'behind' THIS recursive call. 
           necessary for outputting a solution'''    
    for i in range(n):
        # checks that current square isn't under attack
        if col != 1 and state[col-2][i] == 0:
            continue
        
        # apply constraints to the following columns
        temp_state = copy.deepcopy(state)
        for j in range(n-col):
            for x in range(n):
                if cons[i][j][x] == 1 and state[col-1 + j][x] == 1:
                    temp_state[col-1 + j][x] = 1
                else:
                    temp_state[col-1 + j][x] = 0

        # checks constraint validity
        zero = [0] * n
        if zero in temp_state:
            continue

        # adds to the stack 
        temp_stack = copy.deepcopy(stack)
        temp_stack.append((col, i+1))

        if col == n:
            global sols
            sols.append(temp_stack)
        else:
            backtrackin(col + 1, temp_state, temp_stack, n)


def parse_sols(sols: List[List[tuple]], n: int):
    '''
    prunes sols to be unique. a unique solution can't be represented
    as any rotation/reflection of another solution \n
    sols: list of solutions
    n: length of the board'''
    i = 0
    while i < len(sols):
        vars = gen_variants(sols[i], n)
        sols[i].sort()
        if sols[i] in vars:
            vars.remove(sols[i])
        for v in vars:
            if v in sols:
                sols.remove(v)
        i += 1

def gen_variants(sol: List[tuple], n: int) -> List[List[tuple]]:
    '''
    generates all variants of a specific solution (at most, 7) & 
    returns em as a list \n
    sol: the solution (in the form of a list of coordinates)
    n: board length'''
    variants = []

    variants.append([(x[0], n+1-x[1]) for x in sol])
    for i in range(3):
        sol = rotate(sol, n)
        sol.sort()
        if sol not in variants:
            variants.append(sol)

        flip = [(x[0], n+1-x[1]) for x in sol]
        flip.sort()
        if flip not in variants:
            variants.append(flip)

    return variants

def rotate(sol: List[tuple], n: int) -> List[tuple]:
    '''
    rotates a list of chessboard coordinates by 90° clockwise; 
    helper method to gen_variants()\n
    sol: the list of coordinates/a solution to this problem
    n: n'''
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
            copy_sol[i] = (int(x_), int(y_))
    return copy_sol


solution(11)
parse_sols(sols, 11)

print(sols)
print(len(sols))
