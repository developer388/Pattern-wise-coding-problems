'''
Print all subsequence of a given string.
'''

def subsequence(string, i, current_string, result):
    
    if i > (len(string) - 1):
        result.append(current_string)
        return
    
    subsequence(string, i + 1, current_string + string[i], result)
    
    subsequence(string, i + 1, current_string, result)
    
   
    
    
result = []

subsequence('abc', 0, '', result)

print('Result : ', result)

'''
Find length of maximum increasing subsequence of numbers given in an array 
'''
def subsequence(array, current_index, previous_index):
    
    if current_index > (len(array) - 1):
        return 0
    
    take = 0
    
    if previous_index == -1 or array[current_index] > array[previous_index]:
        take = 1 + subsequence(array, current_index + 1, current_index)
    
    not_take = 0 + subsequence(array, current_index + 1, previous_index)
    
   
    return max(take, not_take)
    
result = []

#subsequence('abc', 0, '', result)

result = subsequence([50, 3, 10, 7, 40, 80], 0, -1)



print('Result : ', result)





'''
Use of memoization to decrease the time complexity
'''
def subsequence(array, current_index, previous_index, memo):
    
    key = str(current_index) + ',' + str(previous_index)
    
    
    if current_index > (len(array) - 1):
        return 0
    
    if key in memo:
        return memo[key]
    
    take = 0
    
    if previous_index == -1 or array[current_index] > array[previous_index]:
        take = 1 + subsequence(array, current_index + 1, current_index, memo)
    
    not_take = 0 + subsequence(array, current_index + 1, previous_index, memo)
    
    memo[key] = max(take, not_take)
    
    return memo[key]
    
result = []

#subsequence('abc', 0, '', result)
memo = {}
result = subsequence([50, 3, 10, 7, 40, 80], 0, -1, memo)



print('Result : ', result)



# https://www.youtube.com/watch?v=MYHajVcnXSA