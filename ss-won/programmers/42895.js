function solution(N, number) {
  let answer = -1;
  let cache = Array(9);
  cache.fill([]);
  let cur = 0;
  for (let i = 1; i <= 8; i++) {
    cur = cur * 10 + N;
    cache[i] = [cur];
  }
  for (let i = 1; i <= 8; i++) {
    for (let j = 1; j < i; j++) {
      for (let left of cache[j]) {
        for (let right of cache[i - j]) {
          cache[i].push(left + right);
          cache[i].push(left - right);
          cache[i].push(left * right);
          if (right !== 0) cache[i].push(parseInt(left / right, 10));
        }
      }
    }
    if (cache[i].includes(number)) return i;
  }
  return answer;
}
