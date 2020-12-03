const numSplit = (size, arr) => {
  let tmp = [];
  for (let id = 0; id < arr.length; id += size) {
    let lastId = id + size < arr.length ? id + size : arr.length;
    tmp.push(arr.slice(id, lastId).join(""));
  }
  return tmp;
};

const makeString = (arr) => {
  let loop = 1;
  let str = arr.reduce((acc, v, i) => {
    if (i == arr.length - 1) {
      acc += loop == 1 ? v : loop + v;
      return acc;
    }
    if (v == arr[i + 1]) {
      loop++;
    } else {
      acc += loop == 1 ? v : loop + v;
      loop = 1;
    }
    return acc;
  }, "");
  return str;
};

const solution = (s) => {
  let answer = s.length;
  let arr = s.split("");
  let res = [];

  /*문자열 나눔 구간*/
  for (let size = 1; size <= s.length / 2; size++) {
    res = numSplit(size, arr);
    answer = answer > makeString(res).length ? makeString(res).length : answer;
  }

  return answer;
};
