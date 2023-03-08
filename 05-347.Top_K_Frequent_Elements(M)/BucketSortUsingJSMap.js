// APPROACH - Same as BucketSort.js (first take a look at BucketSort.js) but using Map instead of object
//Reference - https://leetcode.com/problems/top-k-frequent-elements/solutions/669782/javascript-no-sorting-o-n-time/?q=javascript&orderBy=most_votes

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
  const freq_counter = {}
  const bucket = []
  const kFrequentElements = []

  for (let num of nums) {
    freq_counter[num] = (freq_counter[num] || 0) + 1
  }

  for (let [num, freq] of Object.entries(freq_counter)) {
    bucket[freq] = bucket[freq] || []
    //  bucket[freq] = (bucket[freq] || []).push(num) must not be done because push returns length of elements in array so then bucket[freq] left side becomes 1 which is wrong
    bucket[freq].push(num)
  }

  for (let i = bucket.length - 1; i > 0; i--) {
    const elements = bucket[i]
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
