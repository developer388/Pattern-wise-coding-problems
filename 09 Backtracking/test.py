def solution():
	arr = [5, 4, -1, 7, 8]
	

	result = []
	for k in range(len(arr)):
		for i in range(k, len(arr)):
			subarray = []
			for j in range(k, i+1):

				subarray.append(arr[j])
			result.append(subarray)

	print(result)

solution()