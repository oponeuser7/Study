/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    return n<2 ? n : fib(n-1)+fib(n-2);
};
