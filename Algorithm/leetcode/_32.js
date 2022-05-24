/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
    let stack = [];
    let max_l = 0;
    stack.push(-1);
    for(let i=0; i<s.length; i++) {
        if(s[i]==='(') {
            stack.push(i);
        } else {
            stack.pop();
            if(stack.length===0) {
                stack.push(i);
            } else {
                max_l = Math.max(i-stack[stack.length-1], max_l);
            }
        }
    }
    return max_l;
};
