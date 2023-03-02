// APPROACH Bruteforce  - Time O(N^2), Space O(1) - WONT BE ACCEPTED AS IT HAS N^2 Time

const containsDuplicate = (nums) => {
  for (let i = 0; i < nums.length - 1; i++) {
    for (j = i + 1; j < nums.length; j++) {
      if (nums[i] === nums[j]) return true
    }
  }
  return false
}

const nums = [1, 2, 3, 1]
const result = containsDuplicate(nums)
console.log(result)
