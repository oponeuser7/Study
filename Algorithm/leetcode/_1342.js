/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num) {
    let ans = 0;
    while(num>0) {
        if(num&1===1) {
        num -= 1;
        } else {
        num = num>>1;
        }
        ans += 1;
    }
    return ans;
};
