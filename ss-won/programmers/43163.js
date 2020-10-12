function ckchange(cur, tar) {
    let arr = [];
    arr = [...cur];
    return arr.reduce((acc, v, i) => (v != tar[i]) ? acc + 1 : acc, 0);
}

function solution(begin, target, words) {
    let answer = 0;
    if (!words.includes(target))
        return answer;

    const visited = [];
    const q = [];
    q.push([begin, 0]);
    while (q.length != 0) {
        let [curr, count] = q[0]; q.shift();
        if (curr === target) {
            answer = count;
            break;
        }
        for (let word of words) {
            if (!visited.includes(word) && ckchange(curr, word) <= 1) {
                q.push([word, count + 1]);
                visited.push(word);
            }
        }
    }
    return answer;
}
