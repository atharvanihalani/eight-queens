from typing import List
import numpy as np
import copy

'''
notes:
    n increases => more possible solutions
    greater dimension => more possible solutions

'''


sols = []

def transpose(arr: List[List[int]]) -> List[List[int]]:
    new_arr = []
    for i in range(len(arr[0])):
        new_arr.append([])
        for j in range(len(arr)):
            new_arr[i].append(arr[j][i])
            
    return new_arr


def solution(n: int):
    choose_row = [[[0, 0], [0, 1], [0, 2], [0, 3]], 
                  [[1, 0], [1, 1], [1, 2], [1, 3]], 
                  [[2, 0], [2, 1], [2, 2], [2, 3]], 
                  [[3, 0], [3, 1], [3, 2], [3, 3]]]
    state = [[[1 for _ in range(n)] for __ in range(n)] for ___ in range(n)]
    backtrackin(0, state, [], choose_row, 4)
    print(sols)


def backtrackin(slice: int, state: List[List[List[int]]], stack: List[tuple], c_row: List[List[List[int]]], n: int):
    for i in range(len(c_row)):
        for j in range(len(c_row[i])):
            rn = (c_row[i][j][0], c_row[i][j][1])
            if state[slice][rn[0]][rn[1]] == 0:
                continue

            temp_state = copy.deepcopy(state)
            # propagate constraints
            for k in range(n-slice-1):
                if rn[0]+(k+1) < n:
                    if rn[1]+(k+1) < n:
                        temp_state[slice+k+1][rn[0]+(k+1)][rn[1]+(k+1)] = 0
                    if rn[1]-(k+1) >= 0:
                        temp_state[slice+k+1][rn[0]+(k+1)][rn[1]-(k+1)] = 0
                
                if rn[0]-(k+1) >= 0:
                    if rn[1]+(k+1) < n:
                        temp_state[slice+k+1][rn[0]-(k+1)][rn[1]+(k+1)] = 0
                    if rn[1]-(k+1) >= 0:
                        temp_state[slice+k+1][rn[0]-(k+1)][rn[1]-(k+1)] = 0                        


            if [[0 * n]*n] in temp_state:
                continue
            temp_stack = copy.deepcopy(stack)
            temp_stack.append((slice, rn[0], rn[1]))

            if slice == n-1:
                sols.append(temp_stack)
            else:
                temp_row = copy.deepcopy(c_row)
                temp_row.pop(i)
                temp_row = transpose(temp_row)
                temp_row.pop(j)
                backtrackin(slice+1, temp_state, temp_stack, transpose(temp_row), n)
          

def test_sols(sols: List[List[tuple]]) -> bool:

    # checks that no other queen is on the same 'slice'
    for sol in sols:
        if len(sol) != 4:
            return False
        
        tp = transpose(sol)
        for point in tp:
            if len(point) != len(set(point)):
                return False
    
    # checks that no other queen is on the same diagonal
    for sol in sols:

        for point in range(len(sol)):
            diagonals = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
            for i in range(point + 1, len(sol)):
                pass


        # for point in range()
        pass
        
        # for point in range(len(sol)):
        #     d1 = [1, 1]
        #     d2 = [1, -1]
        #     d3 = [-1, -1]
        #     d4 = [-1, 1]

        #     for i in range(point + 1, len(sol)):
        #         if (sol[i][0], sol[point][1] + d1[0], sol[point][2] + d1[1]) == sol[i] or \
        #             (sol[i][0], sol[point][1] + d2[0], sol[point][2] + d2[1]) == sol[i] or \
        #             (sol[i][0], sol[point][1] + d3[0], sol[point][2] + d3[1]) == sol[i] or \
        #             (sol[i][0], sol[point][1] + d4[0], sol[point][2] + d4[1]) == sol[i]:
        #             return False
        #         d1 = [d1[0] + 1, d1[1] + 1]
        #         d2 = [d2[0] + 1, d2[1] - 1]
        #         d3 = [d3[0] - 1, d3[1] - 1]
        #         d4 = [d4[0] - 1, d4[1] + 1]
        # pass
    return True

test = [[(0, 0, 0), (1, 1, 2), (2, 3, 1), (3, 2, 3)], 
        [(0, 0, 0), (1, 1, 2), (2, 3, 3), (3, 2, 1)],
        [(0, 0, 0), (0, 1, 1), (2, 3, 1), (3, 2, 3)]]


# print(test_sols(test))

eg = [3, 7]
print(2*[eg])

# solution(4)


