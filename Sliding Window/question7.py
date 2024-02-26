'''

Given a string and a pattern, find out if the string contains any permutation of the pattern.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.


https://leetcode.com/problems/permutation-in-string/
'''
'''
 Observation :

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
         we have found the match

'''

def solution2(pattern, string):

    map = {}

    for char in pattern:
        if char not in map:
            map[char] = 1
        else:
            map[char] += 1

    first_pointer = 0
    second_pointer = 0
    match = 0

    for second_pointer in range(len(string)):

        second_ptr_char = string[second_pointer]

        if second_ptr_char in map:
            map[second_ptr_char] -= 1
            
            if map[second_ptr_char] >= 0:
                match+=1
        
        if second_pointer > (len(pattern)-1):
            
            first_ptr_char = string[first_pointer]

            if first_ptr_char in map:
                if map[first_ptr_char] >= 0:
                    match -= 1
                
                map[first_ptr_char] +=1

            first_pointer+=1

        if match == len(pattern):
            return True
        
    return False


print('Result: ', solution2('aab', 'aaodaaicf'))