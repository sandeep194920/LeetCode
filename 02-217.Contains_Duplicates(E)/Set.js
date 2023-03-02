//  APPROACH Set - Time O(N), Space O(N)
const containsDuplicate = (nums) => {
  const uniqueElementsSet = new Set(nums) // takes nums array and gives a set of unique elements

  if (nums.length === uniqueElementsSet.size) return false
  return true
}

const nums = [1, 2, 3, 1]
const result = containsDuplicate(nums)
console.log(result)
