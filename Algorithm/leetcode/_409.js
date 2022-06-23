/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {   
  const l = new Array(26).fill(0);
  const u = new Array(26).fill(0);
  let flag = false;
  let ans = 0;

  for(let i=0; i<s.length; i++) {
    const c = s[i];
    if(c.toUpperCase()===c) {
      u[c.charCodeAt(0)-65] += 1;
    } else {
      l[c.charCodeAt(0)-97] += 1;
    }
  }
  
  for(let i=0; i<26; i++) {
    if(l[i]>0) flag = true;
    ans += parseInt(l[i]/2);
  }
  for(let i=0; i<26; i++) {
    if(u[i]>0) flag = true;
    ans += parseInt(u[i]/2);
  }

  ans *= 2;
  if(flag) ans++;

  return ans;
};

console.log(longestPalindrome("abccccdd"));
