'''
Given an array of characters where each character represents a fruit tree, 
you are given two baskets and your goal is to put maximum number of fruits in each basket. 
The only restriction is that each basket can have only one type of fruit. 
You can start with any tree, but once you have started you can’t skip a tree. 
You will pick one fruit from each tree until you cannot, i.e., you will stop 
when you have to pick from a third fruit type. 

Write a function to return the maximum number of fruits in both the baskets.

Example 1:

	Input: Fruit=['A', 'B', 'C', 'A', 'C']
	
	Output: 3
	
	Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:

	Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
	
	Output: 5
	
	Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']


Leetcode URL: https://leetcode.com/problems/fruit-into-baskets/
'''

'''
Solution 1: Optimized Approach 1
    
    Approach Info:

		window size is not fixed

		use a hashmap

		second pointer will add a character to the map

		our window can contain only two unique characters
		
		while len(map) > k:
			decrement character frequency pointed by first_pointer
			if character frequency becomes 0, then delete it from map

		    increment the first_pointer

		result = max(result, window_size)
'''       
 

def mainSolution(array):

	first_pointer = 0
	second_pointer = 0

	result = 0

	map = {}

	for second_pointer in range(len(array)):

		if array[second_pointer] not in map:
			map[array[second_pointer]] = 1
		else:
			map[array[second_pointer]] += 1

		while len(map)>2:
			map[array[first_pointer]] -= 1

			if map[array[first_pointer]] == 0:
				del map[array[first_pointer]]

			first_pointer +=1


		result = max(result, (second_pointer-first_pointer)+1)

	return result

print('Result using MainSolution:', mainSolution(['A', 'B', 'C', 'B', 'B', 'C']))
