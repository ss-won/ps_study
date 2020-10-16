// 코딩테스트 고득점 Kit(DFS/BFS) - 타겟 넘버(43165)
function solution(numbers, target) {
  let answer = 0;
  answer = getmethods(numbers, 0, target);
  return answer;
}

function getmethods(arr, curr, target) {
  let res;
  if (arr.length === 0) return curr === target ? 1 : 0;
  const narr = arr.filter((v, i) => i != 0);
  return (res =
    getmethods(narr, curr + arr[0], target) +
    getmethods(narr, curr - arr[0], target));
}
