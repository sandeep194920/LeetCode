// Approach Hashmap -  Time O(N), Space O(N)
const containsDuplicate = (nums) => {
  const storage = {} // time complexity o(1) if we use hash table like this

  for (let n of nums) {
    // if contains in list
    if (n in storage) {
      return true
    }

    // if not contains in list
    else {
      storage[n] = 1
    }
  }
  return false
}

const nums = [1, 2, 3, 1]
const result = containsDuplicate(nums)
console.log(result)
