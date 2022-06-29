/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var transpose = function(matrix) {
    let ans = new Array(matrix[0].length).fill(null).map(() => new Array(matrix.length));
	for(let i=0; i<matrix[0].length; i++) {
		for(let j=0; j<matrix.length; j++) {
			ans[i][j] = matrix[j][i];
		}
	}
	return ans;
};
