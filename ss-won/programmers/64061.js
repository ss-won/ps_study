const solution = (board, moves) => {
  let answer = 0;
  let bucket = [];
  let box = board
    .reduce((acc, val) => val.map((v, row) => [...(acc[row] || []), v]), [])
    .map((v) => v.filter((i) => i != 0));

  for (let n of moves) {
    if (box[n - 1].length == 0) continue;
    let doll = box[n - 1].shift();
    if (bucket[bucket.length - 1] == doll) {
      answer += 2;
      bucket.pop();
    } else {
      bucket.push(doll);
    }
  }

  return answer;
};

/*
***
 @Test
***
console.log(solution([
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1]
], [1, 5, 3, 5, 1, 2, 1, 4]));
*/
