'''
Given a set with distinct elements, find all of its distinct subsets.

Example 1:

Input: [1, 3]
Output: [], [1], [3], [1,3]
Example 2:

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
'''


def solution(array):
    
    result = []
    
    result.append([]) 
    
    for num in array:        
        n = len(result)
        for i in range(n):          
           subset = list(result[i])
           subset.append(num)
           result.append(subset)

        

    return result, len(result)



# def recursiveSolution(array):
#     result = [[]]
#     recursiveCall(array, 0, result)
#     return result

# def recursiveCall(array, index, result):
    
#     if index == len(array):
#         return

#     for j in range(len(result)):
#         subset = list(result[j])
#         subset.append(array[index])
#         result.append(subset)
    
#     recursiveCall(array, index+1,  result)


def recursiveSolution(array):
    result = []
    recursiveCall(array, 0, [], result)
    return result


def recursiveCall(array, index, subset, result):
    result.append(list(subset))
    
    print(f'loop {index} to 2')
    for i in range(index, len(array)):
        subset.append(array[i])
        print(f'recursive({i+1}, {subset}, {result})')
        recursiveCall(array, i+1, subset, result)
        print(f'return from recursive({i+1}, {subset}, {result}')
        subset.pop()

    print(f'loop end return from recursive({index, subset, result})')


print('Result: ', recursiveSolution([1,2,3]))

#print('Result: ', solution([1, 3]))
#print('Result: ', solution([1, 2, 3, 4]))



# for i in range(1,3):
#     print('ASDD ', i)


# def recursive(index, result):
#     result.append(index)

#     print(f'loop {index} to 2')        
#     for i in range(index, 3):
#         print(f'recursive({i+1})')
#         recursive(i+1, result)
#         print(f'return from recursive({i+1})')

#     print('loop completed ')




# def caller():
#     result = []
#     recursive(1, result)
#     return result


# print('Result: ', caller())