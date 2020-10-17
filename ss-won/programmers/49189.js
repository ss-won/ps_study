function solution(n, edge) {
  let answer = 0,
    mx = 0;
  const q = [];
  const visited = [];
  const adj = {};

  for (let [u, v] of edge) {
    adj[u] = !adj[u] ? [v] : [...adj[u], v];
    adj[v] = !adj[v] ? [u] : [...adj[v], u];
  }

  q.push([1, 0]);
  visited.push(1);
  while (q.length != 0) {
    let [cur, h] = q.shift();
    if (h > mx) {
      mx = h;
      answer = 1;
    } else if (h === mx) {
      answer++;
    }

    if (!adj[cur]) continue;
    for (let next of adj[cur]) {
      if (!visited.includes(next)) {
        visited.push(next);
        q.push([next, h + 1]);
      }
    }
  }
  return answer;
}
