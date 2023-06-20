from typing import List
import numpy as np
import copy

'''
notes:
    n increases => more possible solutions
    greater dimension => more possible solutions

'''





class FourCubed:
    def __init__(self) -> None:
        self.sols = []

    def transpose(self, arr: List[List[int]]) -> List[List[int]]:
        new_arr = []
        for i in range(len(arr[0])):
            new_arr.append([])
            for j in range(len(arr)):
                new_arr[i].append(arr[j][i])
                
        return new_arr
    
    def solution(self, n: int):
        choose_row = [[[0, 0], [0, 1], [0, 2], [0, 3]], 
                      [[1, 0], [1, 1], [1, 2], [1, 3]], 
                      [[2, 0], [2, 1], [2, 2], [2, 3]], 
                      [[3, 0], [3, 1], [3, 2], [3, 3]]]
        state = [[[1 for _ in range(n)] for __ in range(n)] for ___ in range(n)]
        self.backtrackin(0, state, [], choose_row, 4)
        print(self.sols)
        pass

    def backtrackin(self, slice: int, state: List[List[List[int]]], stack: List[tuple], c_row: List[List[List[int]]], n: int):
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
                    self.sols.append(temp_stack)
                else:
                    temp_row = copy.deepcopy(c_row)
                    temp_row.pop(i)
                    temp_row = self.transpose(temp_row)
                    temp_row.pop(j)
                    self.backtrackin(slice+1, temp_state, temp_stack, self.transpose(temp_row), n)
                

four = FourCubed()
four.solution(4)
