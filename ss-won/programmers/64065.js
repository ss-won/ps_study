function solution(s) {
  let answer = [];
  s = s.substring(1, s.length - 1);
  let open = s.indexOf("{");
  let close = s.indexOf("}");
  let block;
  let arr = [];

  let ck = function (v) {
    v = parseInt(v);
    for (let val of answer) {
      if (parseInt(val) == v) return false;
    }
    return true;
  };

  //{,}기준으로 나눠서 배열에 넣기
  while (open != -1 || close != -1) {
    block = s.substring(open + 1, close);
    arr.push(block.split(","));
    open = s.indexOf("{", close + 1);
    close = s.indexOf("}", close + 1);
  }
  //length크기만큼 오름차순 정렬
  arr.sort((a, b) => a.length - b.length);

  arr.forEach((v) => {
    v.forEach((val) => {
      if (ck(val)) answer.push(parseInt(val));
    });
  });

  return answer;
}
