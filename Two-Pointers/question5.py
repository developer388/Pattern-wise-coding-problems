'''
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.


https://leetcode.com/problems/3sum/

Approach:
    Use three pointers  

'''



def solution(array, target):

    array.sort()

    print('array: ', array)

    result = []

    for first_pointer in range(len(array)-2):
            
            if first_pointer>0 and array[first_pointer] == array[first_pointer-1]:
                first_pointer+=1
                continue

            second_pointer = first_pointer + 1
            third_pointer = len(array) - 1

            required_two_pointer_sum = target - array[first_pointer]


            while second_pointer < third_pointer:
                two_pointer_sum = array[second_pointer] + array[third_pointer]
                if two_pointer_sum > required_two_pointer_sum:
                    third_pointer -= 1
                elif two_pointer_sum < required_two_pointer_sum:
                    second_pointer += 1
                else:
                    result.append([array[first_pointer], array[second_pointer], array[third_pointer]])
                    second_pointer += 1
                    third_pointer -= 1

                    while second_pointer<third_pointer and array[second_pointer] == array[second_pointer-1]:
                        second_pointer += 1
                    
                    while third_pointer < len(array)-2 and array[third_pointer] == array[third_pointer+1]:
                        third_pointer -= 1
                        

    return result


print('Result: ', solution([-3, 0, 1, 2, -1, 1, -2], 0))


print('Result: ', solution([-5, 2, -1, -2, 3], 0))
