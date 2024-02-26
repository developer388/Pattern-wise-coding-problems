'''
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.



https://leetcode.com/problems/max-consecutive-ones-iii/

 observation:
    1. window size is not fixed
    2. maintain a counter variable for count of zeroes
    3. if count_of_zeroes exceeds k, start incrementing the first pointer.


'''



def solution(array, k):

    count_of_zeroes = 0

    first_pointer = 0
    second_pointer = 0

    result = 0

    for second_pointer in range(len(array)):

        if array[second_pointer] == 0:
            count_of_zeroes += 1
  
        while count_of_zeroes>k:                
            if array[first_pointer] == 0:
                count_of_zeroes-=1

            first_pointer+=1

        result = max(result, (second_pointer-first_pointer)+1)
        print('f:',first_pointer, 's:',second_pointer, 'a[s]:', array[second_pointer])

    return result


        

print('Result: ', solution([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))