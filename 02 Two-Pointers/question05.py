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
'''


'''
Solution 1: Brute Force Approach
    
    In this approach we are using three nested loops, and if sum of a triplet indicated by i, j, k is 0
    
    we are first sorting the found triplet and then checking it if it exists in our result array
        this way we will avoid duplicate triplet in our result


Time Complexity: O(n^3)
'''


def bruteForceSolution(array):

    result = []
    
    for i in range(len(array)-2):
        
        for j in range(i+1, len(array)-1):
            
            for k in range(j+1, len(array)):
                
                if (array[i] + array[j] + array[k] == 0):
                    
                    triplet = [array[i],array[j],array[k]]
                    
                    triplet.sort()
                    
                    if triplet not in result:
                        result.append([array[i],array[j],array[k]])
                    
    return result
    
    
print("Result using BruteForceSolution: ",  bruteForceSolution([-3, 0, 1, 2, -1, 1, -2]))



'''
Solution 2: Optimized Approach

    If we sort the given array, we can take advantage of two pointer approach to efficiently find a triplet

    we have first_pointer starting from 0 to array.length - 2 and

    a second_pointer and third_pointer starting from first_pointer + 1 and end of the array respectively.

    if first_pointer + sum_two_pointers equals zero we have found our triplet

    if sum of first_pointer + sum_two_pointers is less than zero 
        we have to increase the second_pointer to increase the sum

    if sum of first_pointer + sum_two_pointers is greater than zero 
        we have to decrease the third_pointer to decrease the sum

    to ensure we don't consider the duplicate triplets, in our result
    we need to put three checks as mentioned in code below


Time Complexity: O(n^2)

The outer loop iterates over each element of the array once, resulting in O(n) iterations.
Inside the outer loop, there's a two-pointer approach that iterates through the remaining elements of the array. 
This also results in O(n) iterations in the worst case.
'''
def mainSolution(array, target):
    
    arr.sort()

    result = []
    
    
    first_pointer = 0
    
    for first_pointer in range(len(arr) - 2):
        
        if first_pointer>0 and arr[first_pointer] == arr[first_pointer-1]:
            first_pointer+=1
            continue

        second_pointer = first_pointer + 1
        third_pointer = len(arr) - 1
        
        while (second_pointer < third_pointer):
            
            two_pointer_sum = arr[second_pointer] + arr[third_pointer]
            
            if (arr[first_pointer] + two_pointer_sum == 0):
                result.append([arr[first_pointer], arr[second_pointer], arr[third_pointer]])
                second_pointer += 1
                third_pointer -= 1

                while second_pointer<third_pointer and arr[second_pointer] == arr[second_pointer-1]:
                    second_pointer += 1
                
                while third_pointer < len(arr)-2 and arr[third_pointer] == arr[third_pointer+1]:
                    third_pointer -= 1

            elif (arr[first_pointer] + two_pointer_sum < 0):
                second_pointer += 1
            else:
                third_pointer -= 1
                
    
    return result


print("Result using mainSolution: ", mainSolution([-3, 0, 1, 2, -1, 1, -2], 0))
print("Result using mainSolution: ", mainSolution([-5, 2, -1, -2, 3], 0))
