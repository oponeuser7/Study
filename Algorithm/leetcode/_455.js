/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function(g, s) {
  g.sort((x,y) => x-y);  
  s.sort((x,y) => x-y);
  let gi = 0; let si = 0;
  let ans = 0;
  while(gi<g.length && si<s.length) {
    if(s[si]>=g[gi]) {
      ans++;
      gi++;
    }
    si++;
  }
  return ans;
};

console.log(findContentChildren([1,2], [1,2,3]));
