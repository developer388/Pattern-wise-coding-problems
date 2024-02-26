'''
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}

If a set has ‘n’ distinct elements it will have n! permutations.

Example 1:

Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
'''

def recursiveSolution(input_array):
    result = []
    recursiveCall(input_array, [], result)
    return result, len(result)
    
    
    
def recursiveCall(input_array, current, result):
    
    if len(current) == len(input_array):
        result.append(list(current))
        return
    
    
    for i in range(len(input_array)):
        
        if input_array[i] in current:
            continue
        
        current.append(input_array[i])
        recursiveCall(input_array, current, result)
        current.pop()
    
    
    
    
    
print('Result: ', recursiveSolution([1,2,3]))

