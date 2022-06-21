/**
 * @param {number[]} heights
 * @param {number} bricks
 * @param {number} ladders
 * @return {number}
 */
var furthestBuilding = function(heights, bricks, ladders) {

  let i;
  const gaps = new Array(heights.length).fill(0);

  for(i=0; i<heights.length-1; i++) {
    gaps[i] = [heights[i+1]-heights[i], i+1];
  }
  gaps.sort((x, y) => y[0]-x[0]);
  console.log(gaps);

  for(i=0; i<heights.length-1; i++) {
    const gap = heights[i+1]-heights[i];
    if(gap<=0) {
      continue;
    } else if(gap>0 && bricks<gap && ladders<=0) {
      break;
    } else if(bricks<gap) {
      ladders--;
    } else {
      for(let j=0; j<ladders.length; j++) {
        if(gaps[j]===gap) {
          ladders--;
          bricks += gap;
          break;
        }
      }
      bricks -= gap;
    }
  }

  return i;
};

console.log(furthestBuilding([1,5,1,2,3,4,10000], 4, 1));
