// APPROACH - Create key for each element 26 alph key method, add it to hashmap as keys - Time O(N K), Space - O(N)

var groupAnagrams = function (strs) {
  const hashmap = {}

  for (let str of strs) {
    // we will create unique key of 26 alph approach
    const keyArray = new Array(26).fill(0)
    for (let char of str) {
      const index = char.charCodeAt() - 97
      keyArray[index]++
    }
    const key = keyArray.join('')
    // now we will check if key exists in hashmap

    if (key in hashmap) {
      // push the string to the existing array (value) against the generated key
      hashmap[key].push(str)
    } else {
      // create the key and a value of array with str inside
      hashmap[key] = [str]
    }
  }
  return Object.values(hashmap)
}

const strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
const result = groupAnagrams(strs)

console.log(result)
