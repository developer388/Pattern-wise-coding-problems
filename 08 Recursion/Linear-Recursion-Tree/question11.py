# Check if a given array is sorted or not.

def solution(arr, lastIndex):

	if lastIndex == 1 and arr[lastIndex] > arr[lastIndex-1]:
		return True


	if arr[lastIndex] > arr[lastIndex-1]:
		return solution(arr, lastIndex-1)
	else:
		return False

arr = [1,3,2,5,6,7,8]
#print('Result: ', solution(arr, len(arr)-1))




def solution2(arr, lastIndex):

	if lastIndex == 0:
		return True

	return arr[lastIndex] > arr[lastIndex-1] and solution2(arr, lastIndex-1)
	
arr = [1,3,5,6,7,8]
print('Result using solution2(): ', solution2(arr, len(arr)-1))
