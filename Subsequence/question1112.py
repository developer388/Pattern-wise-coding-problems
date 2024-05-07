# Given an integer array nums, return the length of the longest strictly increasing subsequence


def solution(arr, sub_array,counter, result, i):

	if i == len(arr):
		return result


	sub_array.append(arr[i])
	
	if len(sub_array) > 0:

		lastIndexOfSubArray = len(sub_array) - 1

		if lastIndexOfSubArray > 0 and sub_array[lastIndexOfSubArray - 1] > sub_array[lastIndexOfSubArray]:
			counter += 1
			result = max(result, counter)
	else:
		counter = 0

	return solution(arr, sub_array, counter, result, i+1)
	
	sub_array.pop()
	return solution(arr, sub_array, counter, result, i+1)
	
	

arr = [10,9,2,5,3,7,101,18, 12]
result = 0
#print('Result: ', solution(arr, [], 0, result, 0))





def solution2(array, currentIndex, previousIndex):
	

	if currentIndex == len(array):
		return 0

	take = 0
	
	if previousIndex == -1 or array[currentIndex] > array[previousIndex]:
		take = 1 + solution2(array, currentIndex+1, currentIndex)
	
	notTake = 0 + solution2(array, currentIndex+1, previousIndex)

	return max(take, notTake)

	

print('Result using solution2: ', solution2(arr, 0, -1)
)