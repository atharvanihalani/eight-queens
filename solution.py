from typing import List
import copy

# big_dict[i][j]
# i: columns 1 through 7
# # j: pos 1 through 8 in that column

big_dict = {
    1: [63, 95, 111, 119, 123, 125, 126],
    2: [31, 175, 183, 187, 189, 190, 191],
    3: [143, 87, 219, 221, 222, 223, 223],
    4: [199, 171, 109, 238, 239, 239, 239],
    5: [227, 213, 182, 119, 247, 247, 247],
    6: [241, 234, 219, 187, 123, 251, 251],
    7: [248, 245, 237, 221, 189, 125, 253],
    8: [252, 250, 246, 238, 222, 190, 126]
}
    

ans = []

def call_solution():
    state = [255, 255, 255, 255, 255, 255, 255]
    solution(1, state, [])

def solution(col: int, state: List[int], stack: List):

    for i in range(8):
        # CHECK VALID VALUE
        if col != 1:
            bin_col = '0'*(8-len(format(state[col-2], 'b'))) + format(state[col-2], 'b')
            if bin_col[i] == '0':
                continue

        # apply constraints to the following columns
        temp_state = copy.deepcopy(state)
        for j in range(8-col):
            temp_state[col-1 + j] = state[col-1 + j] & big_dict[i+1][j]

        # check constraint validity
        if 0 in temp_state:
            continue
        else:
            temp_stack = copy.deepcopy(stack)
            temp_stack.append((col, i+1))
            if col == 7:
                global ans
                ans.append(temp_stack)
            else:
                solution(col + 1, temp_state, temp_stack)
            

    # take the first value in the first column
    # apply the constraints to the next seven columns
    # confirm that 0 is not in any of them (ie. there exist valid combs)
        # if not, return the first column and set the next value, and iterate over
        # else, go on to the second column. 
        # take the first VALID value here, and ...
            # ..repeat..
                # ...if i set a value in the seventh col (and its valid), return it and go to the next val

call_solution()
print(ans)
