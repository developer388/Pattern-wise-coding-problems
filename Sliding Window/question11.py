'''


Given a string and a pattern, find the smallest substring in the given string
 which has all the characters of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec".

Example 2:

Input: String="abdabca", Pattern="abc"
Output: "abc"
Explanation: The smallest substring having all characters of the pattern is "abc".

Example 3:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.

 https://leetcode.com/problems/minimum-window-substring/


 observation:
    window size is not fixed

    approach
       start shrinking window if window_size > len(pattern) -1

        while frequency of first_pointer_character != 1
'''


def solution(string, pattern):

    if len(string) == 0 or len(string)< len(pattern):
        return ''
    print('string: ', string, 'pattern: ', pattern)

    map = {}

    # create frequency map
    for char in pattern:
        if char not in map:
            map[char] = 1
        else:
            map[char] += 1

    print('map: ', map)

    result = ''
    first_pointer = 0
    second_pointer = 0
    match = 0

    sub_string = [0,float('inf')]


    for second_pointer in range(len(string)):

        second_ptr_char = string[second_pointer]

        if second_ptr_char in map:
            map[second_ptr_char] -= 1

            if map[second_ptr_char] >= 0:
                match += 1


        while match == len(pattern):
            current_window_length = (second_pointer - first_pointer)+1

            if current_window_length < sub_string[1]:
                sub_string[0] = first_pointer
                sub_string[1] = current_window_length

            first_ptr_char = string[first_pointer]

            if first_ptr_char in map:
                map[first_ptr_char] +=1
                if map[first_ptr_char] > 0:
                    match-=1
                    
                
            
            first_pointer += 1
    
    if sub_string[1] > len(string):
        return ''
    
    return string[sub_string[0]: sub_string[0]+sub_string[1]]


def solution2(string, pattern):

    map = {}

    for char in pattern:
        if char not in map:
            map[char] = 1
        else:
            map[char] += 1

    match = 0

    first_pointer = 0
    for second_pointer in range(len(string)):

        second_ptr_char = string[second_pointer]

        if second_ptr_char in map:
            map[second_ptr_char] -= 1

            if map[second_ptr_char] >= 0:
                match += 1

        first_ptr_char = string[first_pointer]

        if map[first_ptr_char]>1:
            map[first_ptr_char] -= 1
            first_pointer = second_ptr_char

    return (first_pointer, second_pointer)








print('Result: ', solution2('ADOBECODEBANC', 'ABC'))