'''

Given a string, sort it based on the decreasing frequency of its characters.

Example 1:

Input: "Programming"
Output: "rrggmmPiano"
Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.

Example 2:

Input: "abcbab"
Output: "bbbaac"
Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.

'''

import heapq

def solution(string):

	frequency_map = {}

	for character in string:
		if character not in frequency_map:
			frequency_map[character] = 1
		else:
			frequency_map[character] += 1

	max_heap = []

	for key in frequency_map:
		heapq.heappush(max_heap, (-frequency_map[key], key))

	result = ''

	while max_heap:
		frequency, char = heapq.heappop(max_heap)
		result += (char* abs(frequency))

	return result


print('Result: ', solution("Pprogrammming"))

print('Result: ', solution("abcbab"))