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

    const check = (people, cur) => {
      let count = 0;
      for(let i=0; i<cur; i++) {
        if(people[i][0]>=people[cur][0]) count++;
      }
      return count===people[cur][1];
    }

    let temp = null;
    let cur = null;
    for(let i=0; i<people.length; i++) {
      cur = i;
      while(!check(people, cur)) {
        temp = people[cur-1];
        people[cur-1] = people[cur];
        people[cur] = temp;
        cur--;
      }
    }

    return people;
};

console.log(reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]));