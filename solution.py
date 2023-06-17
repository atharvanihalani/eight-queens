from typing import List
import copy

'''
A recursive backtracking solution to the 8 queens problem

Felt pretty damn good about this one. I'll be elaborating on the deets as 
we step thru the code, but here's a bird's eye view of things:

    The problem - each placed queen propagates some constraints throughout  
    the board. ie. no other queen can be placed on the same row, column, or 
    diagonal. As more queens are placed, the constraints get progressively
    'tighter'. In most cases, one ends up with such restrictive constraints, 
    that there's no room to place any more queens. However, in a select few 
    outcomes, you're able to fit in 8 queens on the board, such that none of
    them are attacking any other. It's these outcomes that we're tryna puzzle out.

    The solution -
        We go column by column, placing a queen down at each step. While doing 
        so, we check that a) the square it's placed on isn't 'under attack', and 
        b) there exist 'valid' squares to place more queens, in the remaining 
        columns to the right.
        The constraints dict encodes the constraints of placing a queen at a 
        particular square.
        solution() is the recursive/backtracking/brute-force (but optimal(?)) method
        that PROPAGATES the constraints of multiple queens.
'''

'''
cons[i][j] tells you how placing a queen at the i'th row (for ANY column)
affects the constraints of the (j+1)'th column to its right. The key (lol) to 
deciphering this, is converting the integers to 8-bit strings. The 1's
represent open spots, while the 0's are squares under attack

eg. cons[2][4] = 189 (10111101). 
    translation: I place a queen at the 2nd row (of any column). This means
    that, in the 5th column to the right of this one, I can't place any queens
    on the 2nd and 7th rows.
'''
cons = {
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

def solution(col: int, state: List[int], stack: List):
    '''
    The recursively backtracking method that iterates through the various permutations.
    This is only faster than an 8! brute force, because it 'prunes' invalid perms early
    and efficiently.
    It places a queen in a valid square, applies constraints to the subsequent columns,
    and, if the constraints aren't 'too' constraining, it recurses (ie. tries to place a 
    queen in the next column). If however, the constraints leave no room for a queen in 
    a future col, it checks the next square in that column.

    col: the current column 
    state: the current state of all constraints. note len(state) = 7, because the first 
           column doesn't rlly have any constraints.
    stack: ie. the state of the board in the levels 'behind' THIS recursive call. 
           necessary for outputting a solution
    '''
    for i in range(8):
        # checks that current square isn't under attack
        if col != 1:
            bin_col = '0'*(8-len(format(state[col-2], 'b'))) + format(state[col-2], 'b') # formats it to an 8-bit string
            if bin_col[i] == '0':
                continue

        # apply constraints to the following columns
        temp_state = copy.deepcopy(state)
        for j in range(8-col):
            temp_state[col-1 + j] = state[col-1 + j] & cons[i+1][j] # propagates constraints by &ing em bit-wise

        # check constraint validity
        if 0 in temp_state:
            continue

        # adds to the stack 
        temp_stack = copy.deepcopy(stack)
        temp_stack.append((col, i+1))

        if col == 7:
            global ans
            ans.append(temp_stack)
            print(temp_stack)
        else:
            solution(col + 1, temp_state, temp_stack)


state = [255, 255, 255, 255, 255, 255, 255] # 255 = 11111111; ie. there are no constraints at the beginning
solution(1, state, [])

# print(ans)