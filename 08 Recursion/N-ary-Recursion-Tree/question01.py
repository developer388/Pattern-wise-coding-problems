'''
Given a string containing digits from 2 to 9, return all possible letter combinations 
that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

  1:""     2:"abc"  3:"def"  
  4:"ghi"  5:"jkl"  6:"mno"
  7:"pqrs" 8:"tuv"  9:"wxyz"

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

'''

def solution(input_digits, digit_mapping, sub_array, result, index):

	if index == len(input_digits):
		result.append(list(sub_array))
		return result


	characters = digit_mapping[input_digits[index]]


	for i in range(len(characters)):
		sub_array.append(characters[i])
		solution(input_digits, digit_mapping, sub_array, result, index+1)
		sub_array.pop()

	return result



digit_mapping = {
  "1":"",     
  "2":"abc",
  "3":"def",  
  "4":"ghi",
  "5":"jkl",
  "6":"mno",
  "7":"pqrs",
  "8":"tuv",
  "9":"wxyz"
}

#print('Result: ', solution("23", digit_mapping,[],[], 0))






def permuationOfCharacters(word, result, index):

  if index == len(word):
    result.append(''.join(word))
    return result


  for i in range(index, len(word)):
    
    word[index], word[i] = word[i], word[index]
    
    permuationOfCharacters(word, result, index+1)
    
    word[index], word[i] = word[i], word[index]
    
  return result



word = ["a","b","c"]

#print('Permutaion of all characters :', permuationOfCharacters(word, [], 0))

def permuationOfCombinationOfWords(words_array, sub_array, result, index):

  if index == len(words_array):
    result.append(''.join(sub_array))
    return result

  word = words_array[index]

  for char in word:

    sub_array.append(char)
    permuationOfCombinationOfWords(words_array, sub_array, result, index+1)
    sub_array.pop()

  return result


print('Permuation of combination of words :', permuationOfCombinationOfWords(["abc", "def"], [], [], 0))
