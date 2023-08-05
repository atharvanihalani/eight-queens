from typing import List

'''
here, i'll be taking a slightly different approach from the 2-dimensional
problem.
    1) i won't be encoding 
    

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

deriv_variants([(0, 0, 0), (1, 1, 2), (2, 3, 1), (3, 2, 3)])
