'''
Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

Example 1:

Input: str1="xy#z", str2="xzz#"
Output: true
Explanation: After applying backspaces the strings become "xz" and "xz" respectively.

Example 2:

Input: str1="xy#z", str2="xyz#"
Output: false
Explanation: After applying backspaces the strings become "xz" and "xy" respectively.

Example 3:

Input: str1="xp#", str2="xyz##"
Output: true
Explanation: After applying backspaces the strings become "x" and "x" respectively. In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
Example 4:

Input: str1="xywrrmp", str2="xywrrmu#p"
Output: true
Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.
'''



def solution(string1, string2):
	print('string1: ', string1, ' string2: ', string2)
	return getActualString(string1) == getActualString(string2)
	


def getActualString(string):

	count_of_hash = 0
	result = ''

	for pointer in range(len(string)-1, -1, -1):

		if string[pointer] == '#':
			count_of_hash +=1
		elif count_of_hash > 0:
			count_of_hash -= 1
		else:
			result = string[pointer] + result

	return result


print('Result: ', solution("xy#z", "xzz#"))
print('Result: ', solution("xp#", "xyz##"))
print('Result: ', solution("xy#z", "xyz#"))
print('Result: ', solution("xywrrmp", "xywrrmu#p"))