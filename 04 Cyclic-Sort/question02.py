'''
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’.
Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, 
find the missing number.

Example 1:

Input: [4, 0, 3, 1]
	   [1, 0, 3, 4]
Output: 2
Example 2:

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7

'''


def mainSolution(array):

	i = 0
	
	while i < len(array):
		correct_index = array[i]

		if array[i] < len(array) and array[i]!=array[correct_index]:
			array[i], array[correct_index] = array[correct_index], array[i]			
		else:
			i+=1
		print(array, i)

	for i in range(len(array)):
		if array[i] != i:
			return i


print('Result using mainSolution: ', mainSolution( [8, 3, 5, 2, 4, 6, 0, 1]))


def solution2(arr):
    
    i = 0
    
    while i < len(arr):
        
        correct_index = arr[i] - 1
        
        if arr[i]!=0 and  i != correct_index:
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
        else:
            i += 1
            
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]+1:
            return arr[i-1] + 1
    return arr
    
print('Result using solution2: ', solution2([8, 3, 5, 2, 4, 6, 0, 1]))