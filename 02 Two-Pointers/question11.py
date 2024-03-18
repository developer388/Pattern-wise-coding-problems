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

'''
Solution 1: Optimized Approach:

we need to write algorithm which can give us string after backspace effect

if put the algorithm code in a function, same algorithm can be used for both strings 

once we have both string after backspace effect, we can compare them to get our result


we can start a loop from the end of the array:
	if ith value has #
	   increment the number_of_hash counter
	else if number_of_hash counter > 0:
		decrement the number_of_hash counter value by 1 
		this way we are skipping the backspaced value
	else:
		add the ith character to result string

'''


def mainSolution(string1, string2):
		
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

	return getActualString(string1) == getActualString(string2)
	

print("Result using mainSolution: ", mainSolution("xy#z", "xzz#"))
print("Result using mainSolution: ", mainSolution("xp#", "xyz##"))
print("Result using mainSolution: ", mainSolution("xy#z", "xyz#"))
print("Result using mainSolution: ", mainSolution("xywrrmp", "xywrrmu#p"))
print("Result using mainSolution: ", mainSolution("xyw#rrmp", "xyw#rrmu#p"))



'''
Solution 2: Alternate Approach (does't work if we have backspace multiple time at different characters)

	
	In first, iteration
		we may think to store last index and count of index in a hash map
	
	In second, iteration
		if a character lies in backspace territory, skip it in adding in result

	this approach is more complex and will not work if we have backspace multiple time at different characters
	hence it is not a correct solution and mentioned here just for brainstorming purpose, why to avoid it
'''

def solution2(string1, string2):
	
	map = {
	    'string1': {
	        'last_index': None,
	        'count': 0
	    },
	    
	    'string2': {
	        'last_index': None,
	        'count': 0
	    }
	    
	}
	
	
	for i in range(len(string1)-1, -1, -1):
	    if string1[i] == '#':
	        map['string1']['last_index'] = i
	        map['string1']['count'] +=1
	
	for i in range(len(string2)-1, -1, -1):
	    if string2[i] == '#':
	        map['string2']['last_index'] = i
	        map['string2']['count'] +=1
	
	result_string1 = ''
	result_string2 = ''
	
	for i in range(len(string1)):
	    if map['string1']['last_index'] is None or i < (map['string1']['last_index'] - map['string1']['count']) or i > ((map['string1']['last_index'] + map['string1']['count'])-1) :
	        result_string1 += string1[i]
	
	for i in range(len(string2)):
	    if map['string2']['last_index'] is None or i < (map['string2']['last_index'] - map['string2']['count']) or i > ((map['string2']['last_index'] + map['string2']['count'])- 1):
	        result_string2 += string2[i]
	
	return (result_string1, result_string2, result_string1 == result_string2, map)
	
			

print("Result using solution2: ", solution2("xy#z", "xzz#"))
print("Result using solution2: ", solution2("xy#z", "xyz#"))
print("Result using solution2: ", solution2("xp#", "xyz##"))
print("Result using solution2: ", solution2("xywrrmp", "xywrrmu#p"))