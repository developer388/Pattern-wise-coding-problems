
// Question 1: print linear no. from 1 to N

function question1(i, n) {
    
    if (i>n) {
        return
    }
    
    console.log('question1: ', i)
    question1(i+1, n)
}

//question1(1, 10)

// Question 2: print no. from N to 1
function question2(i, n) {
    
    if (i<n) {
        return
    }
    console.log('question2: ', i)
    question2(i-1, n)
}

//question2(10, 1)



// Question 3: print no. from 1 to N using backtracking

function question3(i, n) {
  
  if (i==0) {
      return 
  }

  question3(i-1,n)
  console.log(i)
}

//question3(10, 10)

// Question 4: print no. from N to 1 using backtracking


// Question 5: summation
function summation(n) {
    
    if (n == 1) {
        return 1
    }
    
    return n + summation(n-1)
    
}

//console.log('summation: ', summation(5))

// Question 6: Reverse an Array


function reverseArray1(array, start, end) {
    
    if (start>=end) {
        return
    }
    
    let x = arr[start]
    array[start] = array[end]
    array[end] = x
    reverseArray1(array, start+1, end-1)
}

function reverseArray2(array, start) {
    
    let end = (array.length - start) - 1
    
    if (start>=end) {
        return
    }
    
    let x = arr[start]
    array[start] = array[end]
    array[end] = x
    
    reverseArray2(array, start+1)
}



let arr = [1,2,3,4,5,6,7]
//reverseArray1(arr, 0, arr.length-1)

//reverseArray2(arr, 0)
//console.log(arr)


// Question 7: Palindrome or not

function isPalindrome(string, start) {
    
    let end = (string.length - start) - 1
    
    if (start>=end) {
        return true
    }
    
    if (string[start] != string[end]) {
        return false
    }
    
    return isPalindrome(string, start+1)
    
}


//console.log(isPalindrome('C', 0))



// Question 8: x to the power y


function power(x, y) {
    if (y==0) {
        return 1
    }
    
    return x * power(x, y-1)
}

// console.log(power(2, 4))


// Question 9: Print before function call and after function call
function log(x) {
    if (x == 5) {
        return 
    }
    
    
    console.log('ascending order: ', x) 
    log(x+1)
    //console.log('descending order: ', x)
}

// log(1)


//Question 10: fibonacci number


function fibonacci(n) {
    if (n<=1){
        return n
    }
    
    // let a =  fibonacci(n-1)
    // let b =  fibonacci(n-2)
    // console.log('a:'+a+' b:'+b)
    //return a+b
    
    return fibonacci(n-1) + fibonacci(n-2)
}

//console.log(fibonacci(4))

// Question 11: print all subsequence of an array
function subsequence(input_array, index, result) {
    
    if (index >= input_array.length) {
        console.log('res:',result)
        return
    }
    
  //  console.log(result, 'push('+input_array[index]+') i =', index)
    result.push(input_array[index])
    subsequence(input_array, index+1, result)
    result.pop()
    
//console.log(result, 'pop('+input_array[index]+') i =', index)
    subsequence(input_array, index+1, result)
}


//subsequence([3,1,2], 0, [])



// Question 12: print all subsequence whose sum is equal to k

function subsequenceEquivalentToSum(arr, k, index, sum, result) {
    
     if (index >= arr.length) {
        if (sum == k) {
            console.log(result)
        }
        return
    }
    
    result.push(arr[index])
    subsequenceEquivalentToSum(arr, k, index+1, sum+arr[index], result)
    result.pop()
    subsequenceEquivalentToSum(arr, k, index+1, sum, result)
}


//subsequenceEquivalentToSum([1,2,1], 2, 0, 0, [])

// Question 13: print only subsequence whose sum is equal to k

function subsequenceEquivalentToSum2(arr, k, index, sum, result) {
    
     if (index >= arr.length) {
        if (sum == k) {
            console.log(result)
            return true
        }
        return false
    }
    
    result.push(arr[index])
    
    if (subsequenceEquivalentToSum2(arr, k, index+1, sum+arr[index], result)) {
        return true
    }
    
    result.pop()
   
    if (subsequenceEquivalentToSum2(arr, k, index+1, sum, result)) {
        return  true
    }
    
    return false
}


//subsequenceEquivalentToSum2([1,2,1], 2, 0, 0, [])




// Question 14: print count of subsequences whose sum is equal to k

function subsequenceEquivalentToSum3(arr, k, index, sum, result) {
    
     if (index >= arr.length) {
        if (sum == k) {
            return 1
        }
        return 0
    }
    
    result.push(arr[index])
    
    let left = subsequenceEquivalentToSum3(arr, k, index+1, sum+arr[index], result)

    result.pop()
   
    let right = subsequenceEquivalentToSum3(arr, k, index+1, sum, result)

    return left+right
}


//console.log(subsequenceEquivalentToSum3([1,2,1], 2, 0, 0, []))


function sum(arr, target, index, result_array) {
    
    if (target < 0) {
        return
    }
    
    if (target == 0) {
        result_array.push(arr[index])
        return
    }
    
    if (index>=arr.length) {
        return
    }
    
    sum(arr, target-arr[index], index, result_array)
    index = index + 1
    sum(arr, target-arr[index], index, result_array)
    
}

//sum([1,2,4], 8, 0, result)

//console.log(result)




//Question 15: combination sum

function combinationSum(arr, k, index, temp_array, result) {
     if (index == arr.length) {
        if (k == 0) {
            result.push([...temp_array])
        }
        return
     }
    
    if (arr[index] <= k) { 
        temp_array.push(arr[index])
        combinationSum(arr, k-arr[index], index, temp_array, result)
        temp_array.pop()
    }
    combinationSum(arr, k, index+1, temp_array, result)
}


let result = []
combinationSum([2, 3, 6, 7], 7, 0, [], result)

console.log('Result: ', result)




