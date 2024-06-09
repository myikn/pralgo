function solution(wallpaper) {
    var answer = [];
    const tmp = [];
    const arr = wallpaper.map(row => row.split(''));
    
    for (let i=0; i<arr.length; i++) {
        for (let j=0; j<arr[i].length; j++) {
            if (arr[i][j] === '#') {
                tmp.push([i, j])
            }
        }
    }
    
    let minX = Infinity, minY = Infinity;
    let maxX = -Infinity, maxY = -Infinity;
    
    for (const [x, y] of tmp) {
        if (x < minX) minX = x;
        if (y < minY) minY = y;
        if (x > maxX) maxX = x;
        if (y > maxY) maxY = y;
    }
    
    answer.push(minX, minY, maxX+1, maxY+1);
    return answer;
}