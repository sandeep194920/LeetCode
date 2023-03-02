// Approach Hashmap - Time - O(N), Space - O(N)

var isAnagram = function (s, t) {
  /*Make a hashmap of both s and t and then compare those two*/
  const storageS = {}
  const storageT = {}

  if (s.length !== t.length) return false

  for (let i = 0; i < s.length; i++) {
    // For S
    let letterS = s[i]
    if (letterS in storageS) {
      storageS[letterS] += 1
    } else {
      storageS[letterS] = 1
    }

    // For T
    let letterT = t[i]
    if (letterT in storageT) {
      storageT[letterT] += 1
    } else {
      storageT[letterT] = 1
    }
  }

  // compare two hashmaps

  for (let key in storageS) {
    if (storageS[key] !== storageT[key]) return false
  }
  return true
}

const s = 'anagram'
const t = 'nagaram'

const result = isAnagram(s, t)
console.log(result)
