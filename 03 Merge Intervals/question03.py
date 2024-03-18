'''
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Example 1:

	Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
	
	Output: [2, 3], [5, 6], [7, 7]
	
	Explanation: The output list contains the common intervals between the two lists.

Example 2:

	Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]

	Output: [5, 7], [9, 10]

	Explanation: The output list contains the common intervals between the two lists.

Leetcode URL: https://leetcode.com/problems/interval-list-intersections/
'''

'''
Solution 1: Optimized Approach


'''


def mainSolution(arr1, arr2):
    result = []

    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        start = max(arr1[i][0], arr2[j][0])
        end = min(arr1[i][1], arr2[j][1])

        if start <= end:
            result.append([start, end])

        # Move the pointer of the interval with the smaller end time forward
        if arr1[i][1] < arr2[j][1]:
            i += 1
        else:
            j += 1

    return result



print("Result using mainSolution: ", mainSolution([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]]))
print("Result using mainSolution: ", mainSolution([[1, 3], [5, 7], [9, 12]], [[5, 10]]))