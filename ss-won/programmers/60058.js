const isEmpty = (p) => {
  if (p.length == 0) return true;
  else false;
};

const dividing = (p) => {
  let u,
    v = "";
  let parr = p.split("");
  let finished = 0;
  let i = 0;
  do {
    if (parr[i] == "(") finished--;
    else finished++;
    i++;
  } while (finished != 0);

  u = parr.slice(0, i).join("");
  v = parr.slice(i, parr.length).join("");
  return [u, v];
};

const isRight = (u) => {
  let res = 0;
  let size = u.length;
  let tmp = u.split("");
  for (let next of tmp) {
    if (next == "(") res += size;
    else res -= size;
    size--;
  }
  return res;
};

const solution = (p) => {
  let answer = "";
  let u,
    v = "";

  /*1단계*/
  if (isEmpty(p)) return answer;
  /*2단계*/
  let res = dividing(p);
  u = res[0];
  v = res[1];
  /*3단계*/
  if (isRight(u) > 0) {
    //올바른 문자열
    u += solution(v);
    answer += u;
  } else {
    //올바른 문자열이 아님
    let tmp = "";
    tmp += "(";
    tmp += solution(v);
    tmp += ")";
    u = u.slice(1, u.length - 1);
    tmp += u
      .split("")
      .map((v) => {
        if (v == "(") return ")";
        else return "(";
      })
      .join("");
    answer += tmp;
  }
  return answer;
};
