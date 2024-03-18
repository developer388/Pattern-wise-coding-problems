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
'''


'''
Solution 1: Optimized Approach 1
    
    window size is fixed
    
    maintain a character map for pattern
    
    if second_pointer match with pattern_map
        if array[second_pointer] >= 1
            increment the match counter

        decrement the array[second_pointer] frequency in map

    if second_pointer > len(pattern) - 1
           we need to increment the first_pointer to maintain a fixed size window

           if array[first_pointer] match with pattern_map
                if array[first_pointer] >= 0     
                    decrement the match counter

                increment the array[first_pointer] frequency in map
   
   if match == len(pattern)
         push the first_pointer to result array
'''

def mainSolution(string, pattern):

    first_pointer = 0
    second_pointer = 0
    
    map = {}
    
    result = []
    
    for char in pattern:
        if char not in map:
            map[char] = 1
        else:
            map[char] += 1
            
    match = 0

    for second_pointer in range(len(string)):
        
        if string[second_pointer] in map:
            if map[string[second_pointer]] >= 1:
                match += 1
            
            map[string[second_pointer]] -= 1
        
        if second_pointer > (len(pattern)-1):
            if string[first_pointer] in map:
                if map[string[first_pointer]] >= 0: 
                    match -= 1
                
                map[string[first_pointer]] += 1
            
            first_pointer += 1
        

        if match == len(pattern):
            result.append(first_pointer)

    return result


print('Result using mainSolution:', mainSolution('abbcabc', 'abc'))