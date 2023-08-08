from typing import List


cons = {}
sols = []


def populate_constraints(n: int):
    '''
    populates the entire constraints matrix \n
    n: side length'''
    for i in range(n):
        for j in range(n):
            cons[(i, j)] = constraints_at(i, j, n)

def constraints_at(row: int, col: int, n: int) -> List[List[List[int]]]:
    all_slices = []

    # tight 2d constraints for THIS slice
    # factor/recurse this following bit out later
    slice_0 = [[1 for _ in range(n)] for __ in range(n)]
    slice_0[row] = [0 for _ in range(n)]
    for i in range(n):
        slice_0[i][col] = 0

        col_idx_1 = (row - i) + col
        col_idx_2 = (i - row) + col

        if col_idx_1 in range(n):
            slice_0[i][col_idx_1] = 0
        if col_idx_2 in range(n):
            slice_0[i][col_idx_2] = 0
    all_slices.append(slice_0)
    
    # + looser, dissapating constraints for subsequent slices
    # AGAIN, make this next bit faar more tighter
    for l in range(1, n): #for each slice
        slice = [[1 for _ in range(n)] for __ in range(n)]
        slice[row][col] = 0
        if row + l in range(n):
            slice[row + l][col] = 0
        if row - l in range(n):
            slice[row - l][col] = 0
        if col + l in range(n):
            slice[row][col + l] = 0
        if col - l in range(n):
            slice[row][col - l] = 0
        
        if (row + l in range(n)) and (col + l in range(n)):
            slice[row + l][col + l] = 0
        if (row + l in range(n)) and (col - l in range(n)):
            slice[row + l][col - l] = 0
        if (row - l in range(n)) and (col + l in range(n)):
            slice[row - l][col + l] = 0
        if (row - l in range(n)) and (col - l in range(n)):
            slice[row - l][col - l] = 0

        all_slices.append(slice)

    return all_slices


populate_constraints(3)
print(cons)
pass

def solution(n: int):
    # populate constraints
    # 
    pass



def transpose(arr: List[List[int]]) -> List[List[int]]:
    new_arr = []
    for i in range(len(arr[0])):
        new_arr.append([])
        for j in range(len(arr)):
            new_arr[i].append(arr[j][i])
            
    return new_arr

def solution(n: int):
    choose_row = [[[0, 0], [0, 1], [0, 2]], 
                  [[1, 0], [1, 1], [1, 2]], 
                  [[2, 0], [2, 1], [2, 2]]]
    state = [[[1 for _ in range(n)] for __ in range(n)] for ___ in range(n)]
    backtrackin(0, state, [], choose_row, n)
    
def backtrackin(slice: int, state: List[List[List[int]]], stack: List[tuple], c_row: List[List[List[int]]], n: int):
    pass



def parse_sols(sols: List[List[tuple]]):
    '''
    iterates through solutions
    for each one, calculates the 'derivative' of it 
    if it's in the derivative list, continue
    else, extend it by all its variants and append the solution'''

    deriv_list = []
    unique_sols = []
    for sol in sols:
        deriv = [(sol[i+1][1] - sol[i][1], sol[i+1][2] - sol[i][2]) for i in range(len(sol)-1)]
        if deriv in deriv_list:
            continue
        else:
            deriv_list.extend(deriv_variants(sol))
            unique_sols.append(sol)

def deriv_variants(sol: List[tuple]) -> List[List[tuple]]:
    variants = []

    diff_1 = [(sol[i+1][1] - sol[i][1], sol[i+1][2] - sol[i][2]) for i in range(len(sol)-1)]
    variants.append([(i[0], i[1]) for i in diff_1])
    variants.append([(-i[0], -i[1]) for i in diff_1])
    diff_1.reverse()
    variants.append([(i[0], i[1]) for i in diff_1])
    variants.append([(-i[0], -i[1]) for i in diff_1])
        

    print(variants)

    for _ in range(3):
        pass
        # variants.extend(deriv_variants_helper(sol))
        
    

def deriv_variants_helper(sol: List[tuple]) -> List[List[tuple]]:
    variants = []

    diff_1 = [(sol[i+1][1] - sol[i][1], sol[i+1][2] - sol[i][2]) for i in range(len(sol)-1)]
    variants.append([i for i in diff_1])
    variants.append([-i for i in diff_1])
    diff_1.reverse()
    variants.append([i for i in diff_1])
    variants.append([-i for i in diff_1])

    sol_transpose = sorted(sol, key=lambda x: x[1])
    diff_2 = [sol_transpose[i+1][0] - sol_transpose[i][0] for i in range(len(sol)-1)]
    variants.append([i for i in diff_2])
    variants.append([-i for i in diff_2])
    diff_2.reverse()
    variants.append([i for i in diff_2])
    variants.append([-i for i in diff_2])

    return variants

# deriv_variants([(0, 0, 0), (1, 1, 2), (2, 3, 1), (3, 2, 3)])
