'''
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Example:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [
  [1,1,6],
  [1,2,5],
  [1,7],
  [2,6]
]

'''

def solution(input_array, target, sub_array, result, index):
  
  if target == 0:
    result.append(list(sub_array))
    return result

  if index == len(input_array):
    return result

  for i in range(index, len(input_array)):

    if i>index and input_array[i] == input_array[i-1]:
      continue

    if input_array[i] > target:
      break

    sub_array.append(input_array[i])

    solution(input_array, target-input_array[i], sub_array, result, i+1)

    sub_array.pop()
  
  return result 


input_array = [10,1,2,7,6,1,5]
input_array.sort()
print(input_array)

result = []
solution(input_array, 8, [], result, 0)
print('Result: ', result)