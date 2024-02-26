'''

Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".

https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

'''
	Observation
		window size is not fixed

	Approach:
		we can create a frequency map
	
		if a char is already present in map, we will shrink the window
		by incrementing first_pointer, while incrementing decrement char frequency

'''


def solution(string):

	first_pointer = 0
	second_pointer = 0

	result = 0

	map = {}


	for second_pointer in range(len(string)):
		
		second_ptr_char = string[second_pointer]

		if second_ptr_char in map:
			first_pointer = max(first_pointer, map[second_ptr_char]+1)

			print('second_pointer:',second_pointer, second_ptr_char, map[second_ptr_char], map[second_ptr_char]+1)

		map[string[second_pointer]] = second_pointer

		result = max(result, (second_pointer - first_pointer) + 1)

	return result


def solution2(string):

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

		result = max(result, (second_pointer -  first_pointer)+1)

	return result


print('Result1:', solution("abacdbb"))
#print('Result2:', solution2("abaaaccfvdeacb"))