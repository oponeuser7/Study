/**
 * @param {string} s
 * @return {number}
 */
var removePalindromeSub = function(s) {
    const l = s.length;
    for(let i=0; i<l; i++) {
        if(s[i]!==s[l-i-1]) return 2;
    }
    return 1;
};
