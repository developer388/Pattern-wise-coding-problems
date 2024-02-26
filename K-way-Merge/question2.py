'''
Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be 
verified from the merged list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]

Example 2:

Input: L1=[5, 8, 9], L2=[1, 7], K=3
Output: 7
Explanation: The 3rd smallest number among all the arrays is 7.
'''

import heapq

def solution(array, k):

    max_heap = []

    count_of_array = len(array)

    maximum_length_of_array = 0
    index_of_array_with_maximum_length = 0

    for index in range(len(array)):
        
        if len(array[index]) > maximum_length_of_array:
            maximum_length_of_array = len(array[index])
            index_of_array_with_maximum_length = index


    # print(count_of_array, maximum_length_of_array, index_of_array_with_maximum_length)
    for number_index in range(len(array[index_of_array_with_maximum_length])):

        for array_index in range(count_of_array):

            if number_index < len(array[array_index]):

                #print(array_index, number_index,    array[array_index][number_index])
                heapq.heappush(max_heap, -array[array_index][number_index])

                if len(max_heap) > k:
                    heapq.heappop(max_heap)

            print(max_heap)


    return -max_heap[0]


def solution2(array, k):

    min_heap = []
    
    for i in range(len(array)):
        heapq.heappush(min_heap, (array[i][0], (i,0)))
    
    print(min_heap)
    count = 0
    
    while count < k and min_heap:
        
        curr = heapq.heappop(min_heap)
 
        #  i ==> Array Number
        #  j ==> Index in the array number
        i = curr[1][0]
        j = curr[1][1]
 
        # The next element belongs to same array as current.
        if j + 1 < len(array[i]):
            heapq.heappush(min_heap, (array[i][j + 1], (i, j + 1)))
        count += 1
        print(min_heap)

    return array[i][j], count

#print('Result: ', solution([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5))

print('Result: ', solution([[2, 6, 8], [3, 7, 10], [5, 8, 11] ], 5))

  #print('Result: ', solution2([[5, 8, 9], [1, 7]], 3))