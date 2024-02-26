'''
Write a function to return a list of starting indices of the anagrams of the pattern 
in the given string.
Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".


Observation:
	1. window size is fixed
    2. maintain a character frequency map for pattern
    3. if second_pointer match with character in frequency map
            increment the match counter
    4. if second_pointer > len(pattern) - 1
            start incrementing first_pointer

            if first_pointer matches with character in frequency map
                decrement the match counter 
                as we are removing this character from the window
    5. if match == len(pattern)
         push the first_pointer to result array


'''


def solution(string, pattern):

	print('string: ', string, ' pattern:', pattern)

	map = {}
	for char in pattern:
		if char not in map:
			map[char] = 1
		else:
			map[char] += 1


	first_pointer = 0
	second_pointer = 0
	match = 0

	result = []

	for second_pointer in range(len(string)):

		second_ptr_char = string[second_pointer]

		if second_ptr_char in map:
			map[second_ptr_char] -= 1
			
			if map[second_ptr_char] >= 0:
				match += 1


		#start moving first pointer when second pointer exceeds
		#length of patter - 1
		if second_pointer > (len(pattern)-1):

			first_ptr_char = string[first_pointer]

			if first_ptr_char in map:
				if map[first_ptr_char] >= 0:
					match -= 1

				map[first_ptr_char] += 1
			
			first_pointer += 1


		if match == len(pattern):
			result.append(first_pointer)

	return result




print('Solution: ', solution('abbcabc', 'abc'))