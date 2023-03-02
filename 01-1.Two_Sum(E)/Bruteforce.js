// Approach Bruteforce - T O(N^2), S O(1)
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j]
      }
    }
  }
}

const nums = [2, 3, 11, 15]
const target = 14

const result = twoSum(nums, target)
console.log(result)
