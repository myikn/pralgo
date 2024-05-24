function solution(k, score) {
    let answer = [];
    let result = [];

    for (let i = 0; i < score.length; i++) {
        if (result.length < k) {
            result.push(score[i]);
            result.sort((a, b) => a - b);
        } else {
            if (score[i] > result[0]) {
                result.shift();
                result.push(score[i]);
                result.sort((a, b) => a - b);
            }
        }
        answer.push(result[0]);
    }
    return answer;
}