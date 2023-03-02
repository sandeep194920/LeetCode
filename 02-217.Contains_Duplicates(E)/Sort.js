// Time O(N Log N), Space O(1)
const containsDuplicate = (nums) => {
  const sortedNums = nums.sort((a, b) => a - b) // sorted in ascending order
  for (let i = 0; i < sortedNums.length - 1; i++) {
    if (sortedNums[i] === sortedNums[i + 1]) {
      return true
    }
  }
  return false
}

const nums = [1, 2, 3, 1]
const result = containsDuplicate(nums)
console.log(result)
