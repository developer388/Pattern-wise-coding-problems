'''

Given a string and a pattern, find out if the string contains any permutation of the pattern.

Example 1:

    Input: String="oidbcaf", Pattern="abc"
    
    Output: true
    
    Explanation: The string contains "bca" which is a permutation of the given pattern.


Leetcode URL : https://leetcode.com/problems/permutation-in-string/

'''

'''
Solution 1: Optimized Approach 1
    
    Approach Info:
        window size is fixed
        
        first build a frequency map for pattern
            
        maintain a "match_count" variable

        if second_pointer match with character in frequency map
                
                decrement the character frequency
                
                if character frequency >= 0        // because frequency may go negative
                    increment the match counter
        
        if second_pointer > len(pattern) - 1

                if first_pointer matches with character in frequency map
                    decrement the match counter 
                    as we are removing this character from the window

                    increment the first_pointer

        if match == len(pattern)
             return True

'''

def mainSolution(pattern, string):

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

        if string[second_pointer] in map:
            map[string[second_pointer]] -= 1
            
            if map[string[second_pointer]] >= 0:
                match+=1
        
        if second_pointer > (len(pattern)-1):
    
            if string[first_pointer] in map:
                if map[string[first_pointer]] >= 0:
                    match -= 1
                
                map[string[first_pointer]] +=1

            first_pointer+=1

        if match == len(pattern):
            return True
        
    return False


print('Result using MainSolution:', mainSolution('iaa', 'aaodaaicf'))