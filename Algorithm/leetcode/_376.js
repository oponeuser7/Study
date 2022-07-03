/**
 * @param {number[]} nums
 * @return {number}
 */
var wiggleMaxLength = function(nums) {

  const solution = (flag) => {
    const temp = [nums[0]];
    for(let i=1; i<nums.length; i++) {
      if(flag && nums[i-1]>nums[i]) {
        temp.push(nums[i]);
        flag = false;
      }
      else if(!flag && nums[i-1]<nums[i]) {
        temp.push(nums[i]);
        flag = true;
      }
    }
    return temp;
  }

  const ans = solution(false);
  const ans2 = solution(true);

  return Math.max(ans.length, ans2.length);
};

console.log(wiggleMaxLength([3,2,5]));
