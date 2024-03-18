'''
We are given an array containing ‘n’ objects. Each object, when created,
 was assigned a unique number from 1 to ‘n’ based on their creation sequence. 
 This means that the object with sequence number ‘3’ was created just before the 
 object with sequence number ‘4’.

Write a function to sort the objects in-place on their creation sequence number in 
O(n) and without any extra space. For simplicity, let’s assume we are passed an integer 
array containing only the sequence numbers, though each number is actually an object.

Example 1:
Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]


Example 2:
Input: [2, 6, 4, 3, 1, 5]
Output: [1, 2, 3, 4, 5, 6]

Example 3:
Input: [1, 5, 6, 4, 3, 2]
Output: [1, 2, 3, 4, 5, 6]

'''

def mainSolution(arr):
	
	i = 0

	while i < len(arr):
	    

	    correct_index = arr[i] - 1
	    
	    if correct_index != i:
	        arr[i], arr[correct_index] = arr[correct_index], arr[i]
	    else:
	       i+=1
	       
	return arr
	
 
print("Result using mainSolution: ", mainSolution([3, 1, 5, 4, 2]))
print("Result using mainSolution: ", mainSolution( [2, 6, 4, 3, 1, 5]))
print("Result using mainSolution: ", mainSolution( [1, 5, 6, 4, 3, 2]))