'''
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. 
Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

Example 1:

	Jobs: [[1,4,3], [2,5,4], [7,9,6]]
	
	Output: 7
	
	Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the jobs 
	are running at the same time i.e., during the time interval (2,4).

Example 2:

	Jobs: [[6,7,10], [2,4,11], [8,12,15]]

	Output: 15

	Explanation: None of the jobs overlap, therefore we will take the maximum load of any job which is 15.

Example 3:

	Jobs: [[1,4,2], [2,4,1], [3,6,5]]
	
	Output: 8
	
	Explanation: Maximum CPU load will be 8 as all jobs overlap during the time interval [3,4].
'''
'''
	Observation:
		Input is not sorted by start time
'''

def solution1(array):
	
	array.sort()

	start_time = array[0][0]
	end_time = array[0][1]
	cpu_load = array[0][2]
	max_cpu_load = 0

	for i in range(1, len(array)):

		if array[i][0] < end_time:
			end_time = max(end_time, array[i][1])
			cpu_load = cpu_load + array[i][2]
			max_cpu_load = max(cpu_load, max_cpu_load)

		max_cpu_load = max(max_cpu_load, array[i][2])

	return max_cpu_load



print('Result using solution1: ', solution1([[1,4,3], [2,5,4], [7,9,6]]))
print('Result using solution1: ', solution1([[6,7,10], [2,4,11], [8,12,15]]))
print('Result using solution1: ', solution1([[1,4,2], [2,4,1], [3,6,5]]))


def solution2(arr):
    
    arr.sort()
    cpu_load = 0
    
    for interval in range(len(arr)-1):
        next_interval = interval + 1
        
        if arr[interval][1] > arr[next_interval][0]:
            cpu_load = max(cpu_load, arr[interval][2] + arr[next_interval][2])
            arr[next_interval][0] = min(arr[interval][0], arr[next_interval][0])
            arr[next_interval][1] = max(arr[interval][1], arr[next_interval][1])
            arr[next_interval][2] = arr[interval][2] + arr[next_interval][2]
            
        else:
            cpu_load = max(cpu_load, arr[interval][2])
            
    cpu_load = max(cpu_load, arr[len(arr)-1][2])
    
    return cpu_load            

print('Result using solution2: ', solution2([[1,4,3], [2,5,4], [7,9,6]]))
print('Result using solution2: ', solution2([[6,7,10], [2,4,11], [8,12,15]]))
print('Result using solution2: ', solution2([[1,4,2], [2,4,1], [3,6,5]]))