/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSumSetApproach = function(numbers, target) {
    const l = numbers.length;
    const s = new Set(numbers);
    for(let i=0; i<l; i++) {
        const temp = target-numbers[i];
        if(s.has(temp)) {
            for(let j=0; j<l; j++) {
                if(i!=j && numbers[j]===temp) return [i+1, j+1];
            }
        }
    }
};

const twoSumTwoPointersApproach = (numbers, target) => {
    const l = numbers.length;
    let x = 0;
    let y = l-1;
    while(x<y) {
        const temp = numbers[x]+numbers[y];
        if(temp>target) y--;
        else if(temp<target) x++;
        else return [x+1, y+1];
    }
};

const twoSumBinarySearchApproach = (numbers, target) => {
    const length = numbers.length;
    let l = 0; let r = length-1; let temp = 0; let mid = 0;
    for(let i=0; i<length-1; i++) {
        l = i+1;
        r = length-1;
        temp = target-numbers[i];
        while(l<=r) {
            mid = parseInt((l+r)/2);
            if(numbers[mid]>temp) r = mid-1;
            else if(numbers[mid]<temp) l = mid+1;
            else return [i+1, mid+1];
        }   
    }
};
