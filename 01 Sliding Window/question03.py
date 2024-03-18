'''
Given a string, find the length of the longest substring
 in it with no more than K distinct characters.

Example 1:

	Input: String="araaci", K=2

	Output: 4

	Explanation: The longest substring with no more than '2' distinct characters is "araa".

'''

'''
Solution 1: Brute Force Approach

   use a set 

	outer loop from i=0 to i=end of string
	   inner loop from j=i to j=end of string
	      if unique_characters in substring <= k
	      	 result = max(result, len(substring))

'''
def bruteForceSolution(arr, k):
    
    result = 0
    
    for i in range(len(arr)):
        
        word = ''
        
        for j in range(i, len(arr)):
            
            word += arr[j]
            
            distinct_chars = len(set(word))
            
            if distinct_chars <= k:
                result = max(result, len(word))
            
            
    return result
 
    
print("Result using BruteForceSolution: ", bruteForceSolution('araaci', 2))


'''
Solution 2: Optimized Approach 1
    
    Approach Info:

		window size is not fixed

		use a hashmap

		second pointer will add a character to the map
		
		if len(hashmap) > k
			decrement character frequency pointed by first_pointer
			if character frequency becomes 0, then delete it from map

		    increment the first_pointer

		result = max(result, window_size)
'''


def mainSolution(string, k):

	first_pointer  = 0
	second_pointer = 0

	map = {}

	result = 0

	for second_pointer in range(len(string)):

		if string[second_pointer] not in map:
			map[string[second_pointer]] = 1
		else: 
			map[string[second_pointer]] += 1
		
		if len(map) > k:
			
			map[string[first_pointer]] -= 1

			if map[string[first_pointer]] == 0:
				del map[string[first_pointer]]

			first_pointer += 1

		result = max(result, (second_pointer-first_pointer)+1)

	return result


print('Result: ', mainSolution('araaciiiiiiii', 2))

print('Result: ', mainSolution('ababcbcbaa', 2))


