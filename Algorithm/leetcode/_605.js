/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(f, n) {
  let ans = 0;
  let count = 1;
  let flag = false;
  for(let i=0; i<f.length; i++) {
    if(f[i]===0) {
      flag = true;
      count += 1;
      if(i===f.length-1) {
        ans += Math.ceil(++count/2)-1;
      }
    } else if(flag && f[i]===1) {
      ans += Math.ceil(count/2)-1;
      flag = false;
      count = 0;
    } else {
      count = 0;
    }
  }

  return ans>=n;
};

console.log(canPlaceFlowers([1,0,0,0,1], 2));
