// APPROACH - Sort strings and then compare -  Time O(N logN), Space - O(1)

var isAnagram = function (s, t) {
  return s.split('').sort().join('') === t.split('').sort().join('')
}

const s = 'anagram'
const t = 'nagaram'

const result = isAnagram(s, t)
console.log(result)
