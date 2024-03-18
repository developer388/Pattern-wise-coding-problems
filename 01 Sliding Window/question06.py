'''
Given a string with lowercase letters only, if you are allowed to replace no more than 
‘k’ letters with any letter, find the length of the longest substring having the same letters 
after replacement.

Example 1:

    Input: String="aabccbb", k=2

    Output: 5

    Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".


Leetcode URL: https://leetcode.com/problems/longest-repeating-character-replacement/

tagged_as: important

'''

'''
Solution 1: Brute Force Approach
    

'''
def bruteForceSolution(arr, k):
    
    result = 0
    
    for i in range(len(arr)):
        
        word = ''
        map = {}
        
        for j in range(i, len(arr)):
            
            word += arr[j]
            
            if arr[j] not in map:
                map[arr[j]] = 1
            else:
                map[arr[j]] += 1
            
            if len(map) == 2 and 2 in map.values():
                result = max(result, len(word))
            
            
    return result
    
    
print("Result using BruteForceSolution: ", bruteForceSolution("aabccbb", 2))



''' 
Solution 2: Optimized Approach 1
    
    Approach Info:
        observe the input "bbbbbaabbb"

        if we subtract frequency of character with maximum occurence from the window_size
           we will get no. of characters that needs to be replaced to make string with same characters
        
        use a hasmap

        second pointer will add a character to the map

        a variable can be used to store frequency of character with maximum occurence i.e maximum_occurence

        if window_size - maximum_occurence > k
            decrement character frequency in map
            increment the first pointer

        result = max(result, window_size)

'''
def mainSolution(string, k):

    first_pointer = 0
    second_pointer = 0
   
    map = {}

    maximum_occurence = 0

    result = 0

    for second_pointer in range(len(string)):
        
        if string[second_pointer] not in map:
            map[string[second_pointer]] = 1
        else:
            map[string[second_pointer]] += 1
        
        maximum_occurence = max(maximum_occurence, map[string[second_pointer]])

        if ((second_pointer-first_pointer)+1) - maximum_occurence > k:
            map[string[first_pointer]] -= 1
            first_pointer +=1

        result = max(result, ((second_pointer-first_pointer)+1))
    

    return result


print('Result using MainSolution:', mainSolution('abbbbaabbbb', 2))