
// pick or not pick

function task(input_array, result, i, sub_array) {
    
    if (i==input_array.length) {
        result.push([...sub_array])
        return
    }
    
    sub_array.push(input_array[i])
    task(input_array, result, i+1, sub_array)
    
    sub_array.pop()
    task(input_array, result, i+1, sub_array)
}


// print all subsets of an array, which doesn't contain duplicates
function task2(input_array, result, index, sub_array) {
    
    result.push([...sub_array])
    
    for (let i=index;i<input_array.length; i++) {
        sub_array.push(input_array[i])
        task2(input_array, result, i+1, sub_array)
        sub_array.pop()
    }
}


// print all subsets of an array, which contains duplicates
function task3(input_array, result, index, sub_array) {
    
    result.push([...sub_array])
    
    for (let i=index;i<input_array.length; i++) {
        
        if (i==index && input_array[i]==input_array[i-1]) {
            continue
        }
        
        sub_array.push(input_array[i])
        task3(input_array, result, i+1, sub_array)
        sub_array.pop()
    }
}



// print all permutations of a string
function task4(input_array, result, index, sub_array) {
    
    if (sub_array.length == input_array.length) {
        result.push([...sub_array])
        return
    }  
    
    for (let i=0;i<input_array.length; i++) {
        
        if (sub_array.includes(input_array[i])) {
            continue
        }
        
        sub_array.push(input_array[i])
        task4(input_array, result, i, sub_array)
        sub_array.pop()
    }
}



let result = []
task4(['A', 'B', 'C'], result, 0, [] )

console.log(result, result.length)

//Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]