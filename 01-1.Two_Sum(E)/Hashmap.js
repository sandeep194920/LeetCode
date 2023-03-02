// Approach Hashmap - T O(N), S O(N)

var twoSum = function (nums, target) {
  const valIndexMap = {} // value : index

  for (let i = 0; i < nums.length; i++) {
    diff = target - nums[i]

    if (diff in valIndexMap) {
      return [i, valIndexMap[diff]]
    }

    valIndexMap[nums[i]] = i
  }
}

const nums = [2, 3, 11, 15]
const target = 14

const result = twoSum(nums, target)
console.log(result)
