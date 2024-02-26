'''

Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.

Example 1:

Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".

Example 2:

Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".

https://leetcode.com/problems/substring-with-concatenation-of-all-words/

'''


def solution(string, words):

	length_of_word = len(words[0])
	length_of_pattern = length_of_word * len(words)

	print('length_of_word:', length_of_word, 'length_of_pattern:', length_of_pattern)

	map = {}

	for word in words:
		if word not in map:
			map[word] = 0
		else:
			map[word] += 1

	first_pointer = 0
	second_pointer = 0

	match = 0

	for second_pointer in range(first_pointer+(length_of_pattern-1),len(string)):
		print(second_pointer)
		



print('Solution: ', solution('catcatfoxfox', ["cat", "fox"]))