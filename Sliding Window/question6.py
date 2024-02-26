'''

Given a string with lowercase letters only,
if you are allowed to replace no more than ‘k’ letters with any letter, 
find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".


https://leetcode.com/problems/longest-repeating-character-replacement/


    Observation
        window size is not fixed

    


'''


def solution(s, k):

    map = {}

    first_pointer = 0
    second_pointer = 0
    frequency = 0


    result = 0

    for second_pointer in range(len(s)):
        if s[second_pointer] not in map:
            map[s[second_pointer]] = 1
        else:
            map[s[second_pointer]] += 1
        
        frequency = max(frequency, map[s[second_pointer]])

        if ((second_pointer-first_pointer)+1) - frequency > k:
            map[s[first_pointer]] -= 1
            first_pointer +=1

        result = max(result, ((second_pointer-first_pointer)+1))
        print(f'start:{first_pointer}, end:{second_pointer},  result:{result}')
    

    return result


print('Result: ', solution('aaabbbb', 2))