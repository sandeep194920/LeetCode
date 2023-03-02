// APPROACH - Sort each element, add it to hashmap as keys - Time O(N Klog K), Space - O(N)

var groupAnagrams = function (strs) {
  const hashmap = {}

  for (let str of strs) {
    // sort the str and add it to hashmap
    const sortedStr = str.split('').sort().join('')

    if (sortedStr in hashmap) {
      hashmap[sortedStr].push(str)
    } else {
      hashmap[sortedStr] = [str]
    }
  }
  return Object.values(hashmap)
}

const strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
const result = groupAnagrams(strs)

console.log(result)
