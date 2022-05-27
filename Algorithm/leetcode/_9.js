/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    x = x.toString();
    l = x.length;
    for(let i=0; i<parseInt(l/2); i++) {
        if(x[i]!=x[l-1-i]) return false;
    }
    return true;
};
