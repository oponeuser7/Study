/**
 * @param {number[][]} people
 * @return {number[][]}
 */
 var reconstructQueue = function(people) {
    const logic = (x, y) => {
      if(x[1]>y[1]) {
        return 1;
      } else if(x[1]<y[1]) {
        return -1;
      } else {
        return x[0]-y[0];
      }
    }

    people.sort(logic);

    return people;
};

console.log(reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]));