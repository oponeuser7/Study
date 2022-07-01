/**
 * @param {number[]} nums
 * @return {boolean}
 */
var checkPossibility = function(nums) {
  let count = 0;
  let flag = false;
  for(let i=0; i<nums.length; i++) {
    if(i===0 && nums[i]>nums[i+1]) {
      count++;
    } else if(i===nums.length-1 && nums[i-1]>nums[i]) {
      count++;
    } else if(nums[i-1]>nums[i] || 

};
