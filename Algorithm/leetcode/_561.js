/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
  nums.sort((x,y) => x-y);
  let ans = 0;
  for(let i=0; i<nums.length; i++) {
    ans += Math.min(nums[i], nums[i+1]);
    i++;
  }
  return ans;
};
