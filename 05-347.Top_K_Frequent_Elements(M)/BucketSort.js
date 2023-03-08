// APPROACH - Bucket Sort -
/*
- Create a frequency mapping of elements - {each element : times repeated}
- Create an array of length - number of elements + 1. 
    - Loop over frequency map and fill the array. 

Example:
Original array - [a a a a b b b b b c d e e]

freq_map = {
    a:4,
    b:5,
    c:1,
    d:1,
    e:2
}
    [c,d]                  [a]   [b]
__    __    __     __      __     __     __    __    __    __    __    __    __     __
0      1     2      3       4      5      6     7     8     9    10    11    12    13

- Traverse this array from right side and return k elements
*/

var topKFrequent = function (nums, k) {
  const frequencyCounter = {}

  // creating a freq counter here
  for (let num of nums) {
    if (num in frequencyCounter) {
      frequencyCounter[num] += 1
    } else {
      frequencyCounter[num] = 1
    }
  }
  // freq_counter -  { '1': 3, '2': 2, '3': 1 }

  // Bucket sort
  //  const buckets = Array.from({ length: nums.length + 1 }, () => 0)
  const buckets = new Array(nums.length + 1).fill(0)

  for (let [element, bucket] of Object.entries(frequencyCounter)) {
    // key is element and value is bucket in Object.entries(frequencyCounter)
    if (buckets[bucket] === 0) {
      buckets[bucket] = [element]
    } else {
      buckets[bucket].push(element)
    }
  }

  // reverse traverse the buckets and get the first two elements (K)
  //   console.log(buckets)
  const kFrequentElements = []
  for (let i = buckets.length - 1; i > 0; i--) {
    const elements = buckets[i]
    if (elements !== 0) {
      for (let el of elements) {
        kFrequentElements.push(el)
        if (kFrequentElements.length >= k) return kFrequentElements
      }
    }
  }
}

// const nums = [1, 1, 1, 2, 2, 3]
const nums = ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'c', 'd', 'e', 'e']
const k = 2

const result = topKFrequent(nums, k)

console.log(result)
