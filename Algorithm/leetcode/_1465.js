/**
 * @param {number} h
 * @param {number} w
 * @param {number[]} horizontalCuts
 * @param {number[]} verticalCuts
 * @return {number}
 */
var maxArea = function(h, w, horizontalCuts, verticalCuts) {
  const modulo = (x) => Number(x%BigInt(Math.pow(10, 9) + 7));  
  
  horizontalCuts.sort((x,y) => x-y);
  verticalCuts.sort((x,y) => x-y);
  horizontalCuts.push(h);
  verticalCuts.push(w);

  const max = (arr) => {
    let max = 0;
    for(let i=0; i<arr.length; i++) {
      max = arr[i]>max ? arr[i] : max;
    }
    return max;
  };

  const cut = (x, i, arr) => x-(i>0 ? arr[i-1] : 0);

  const rows = horizontalCuts.map(cut);

  const rect = rows.map((row) => {
    const result = verticalCuts.map(cut);
    return result.map((x) => BigInt(row)*BigInt(x));
  });

  const ans = rect.map((x) => max(x));

  return modulo(max(ans));
};

console.log(maxArea(1000000000, 1000000000, [2], [2]));
