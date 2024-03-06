'''
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

	Input: String="aabccbb" 

	Output: 3

	Explanation: The longest substring without any repeating characters is "abc".

Leetcode URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''


''' 
Solution 1: Brute Force Approach
	
	if we store given string in a set, we will get length of string with unique characters

	outer loop from i=0 to i=end of string
	   inner loop from j=i to j=end of string
	      if substring i to j == set(string)
	      	 result = max(result, len(substring))


'''
def bruteForceSolution(arr):
    
    result = 0
    
    for i in range(len(arr)):
        
        word = ''
        
        for j in range(i, len(arr)):
            
            word += arr[j]
            
            if len(word) == len(set(word)):
                result = max(result, len(word))            
            
    return result


print("Result using BruteForceSolution: ", bruteForceSolution("aabccbb"))


'''
Solution 2: Optimized Approach 1

	
	Approach Info:

		use sliding window, window size is not fixed
		shrink the window size using first_pointer
		
		use a hashmap

		second pointer will add a character to the map

		if frequency of a character in map in > 1 then 
			while frequency of the character != 1:
				decrement character frequency in map
				if frequency becomes zero delete from m

		result = max(result, window_size)


'''
def mainSolution(string):

	first_pointer = 0
	second_pointer = 0

	result = 0

	map = {}

	for second_pointer in range(len(string)):

		if string[second_pointer] not in map:
			map[string[second_pointer]] = 1
		else:
			map[string[second_pointer]] += 1

		while map[string[second_pointer]] != 1:
			map[string[first_pointer]] -= 1

			if map[string[first_pointer]] == 0:
				del map[string[first_pointer]]

			first_pointer += 1

		result = max(result, (second_pointer - first_pointer) + 1)

	return result


print('Result using MainSolution:', mainSolution("abacdbb"))



'''
Solution 3: Optimized Approach 2

'''

def Solution3(string):

	first_pointer = 0
	second_pointer = 0

	map = {}
	
	result = 0

	for second_pointer in range(len(string)):
		
		second_ptr_char = string[second_pointer]

		if second_ptr_char in map:
			first_pointer = max(first_pointer, map[second_ptr_char]+1)

			print('second_pointer:',second_pointer, second_ptr_char, map[second_ptr_char], map[second_ptr_char]+1)

		map[string[second_pointer]] = second_pointer

		result = max(result, (second_pointer - first_pointer) + 1)

	return result







    
            



