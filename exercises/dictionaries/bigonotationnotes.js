// ({plugins: ['jsdom-quokka-plugin', 'quokka-jquery-loader']})

const numbers = [4,6,7,4,2,2,4,5,6,7,8,0,9,78,6,7,5,3,1,12,3,45,6,67,7,8,9,8,7,56,45,3,3,2,2,4,5,6,67]

// BIG O NOTATION

// MAKING A DICTIONARY
const numberCounts = {}
numbers.forEach(sourceNumber => {
    if (numberCounts[sourceNumber]) { /* first time through this is false */
        numberCounts[sourceNumber]++
    } else {
        numberCounts[sourceNumber] = 1 /*when it gets a number it sets the counter as 1 and increases */
    }
})
console.log(numberCounts)


// Another Way to do it
numbers.forEach(sourceNumber => {
    let numberOfTimeItExists = 0

    numbers.forEach(targetNumber => {
        if(targetNumber === sourceNumber) {
            numberOfTimeItExists++
        }
    })
    console.log(numberOfTimeItExists)
})