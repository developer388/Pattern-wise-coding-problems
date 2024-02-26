'''

Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]
Example 2:

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]

'''

def solution(array):
    
    result = []
    
    result.append([]) 
    
    start_index = 0
    end_index = 0

    for num_index in range(len(array)):

        start_index = 0
         
        if num_index > 0 and array[num_index] == array[num_index-1]:
            start_index = end_index

        end_index = len(result)
        
        for subset_index in range(start_index, end_index):
                
            subset = list(result[subset_index])
            subset.append(array[num_index])
            result.append(subset)

        print(result, end_index)

    return result

print('Result: ', solution([1, 3, 3]))
#print('Result: ', solution([1, 5, 3, 3]))