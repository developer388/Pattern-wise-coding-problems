# Given a number N, print every digit of the number in words.

import math

def solution(map, number):
	
	if number == 0:
		return ""



	lastDigit = number % 10
	return solution(map, math.floor(number / 10)) + ' ' + map[lastDigit]
	
	 






digit_map = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

print('Result: ', solution(digit_map, 601981))