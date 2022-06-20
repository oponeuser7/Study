/**
 * @param {string[]} words
 * @return {number}
 */
var minimumLengthEncoding = function(words) {

  const getSubstring = (str) => {
    const substring = [];
    for(let i=0; i<str.length-1; i++) {
      for(let j=0; j<str.length-i; j++) {
        let temp = str.slice(j, j+i+1);
        if(j===str.length-i-1) temp += '#';
        substring.push(temp);
      }
    }
    return substring;
  }

  set = new Set();
  wordsSet = new Set();
  ans = '';
  for(let i=0; i<words.length; i++) {
    const substring = getSubstring(words[i]);
    for(let j=0; j<substring.length; j++) {
      set.add(substring[j]);
    }
  }
  for(let i=0; i<words.length; i++) {
    if(set.has(words[i]+'#') || wordsSet.has(words[i])) continue;
    ans += words[i]+"#";
    wordsSet.add(words[i]);
  }

  return ans.length;

};

console.log(minimumLengthEncoding(["time","me","bell"]));
