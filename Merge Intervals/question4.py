'''
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example 1:

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

Example 2:

Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.

Example 3:

Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.


	Observation:
		Input is not sorted


'''
def solution(array):

	array.sort()

	start_time = array[0][0]
	end_time = array[0][1]

	for i in range(1, len(array)):

		if array[i][0] < end_time:
			return False

		start_time = array[i][0]
		end_time = array[i][1]

	return True

print('Solution: ', solution([[1,4], [2,5], [7,9]]))
print('Solution: ', solution([[6,7], [2,4], [8,12]]))
print('Solution: ', solution([[4,5], [2,3], [3,6]]))