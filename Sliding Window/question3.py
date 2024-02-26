'''

Given a string, find the length of the longest substring
 in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

'''
'''
	observation

		window size is not fixed

		for char frequency we can use a map, if len(map)> k, update size of longest substring

		if we encouter new charachter we will start shrinking window, at ith second pointer
		second pointer will remain fixed. we can use a while loop to increment the first_pointer


'''



def solution(string, k):


	first_pointer  = 0
	second_pointer = 0

	char_frequencey = {}

	maximum_substring_length = 0

	for second_pointer in range(len(string)):

		if string[second_pointer] not in char_frequencey:
			char_frequencey[string[second_pointer]] = 1
		else: 
			char_frequencey[string[second_pointer]] += 1
		
		while len(char_frequencey)>k:
			char_frequencey[string[first_pointer]] -= 1

			if char_frequencey[string[first_pointer]] == 0:
				del char_frequencey[string[first_pointer]]

			first_pointer += 1

		maximum_substring_length = max(maximum_substring_length, (second_pointer-first_pointer)+1)

		

	return maximum_substring_length


print('Result: ', solution('araaciiiiiiii', 2))

print('Result: ', solution('ababcbcbaa', 2))


