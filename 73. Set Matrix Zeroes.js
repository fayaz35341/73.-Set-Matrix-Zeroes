/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    let row=new Set()
    let col=new Set()
    let m=matrix.length
    let n=matrix[0].length

    for (let i=0;i<m;i++){
        for (let j=0;j<n;j++){
            if (matrix[i][j]===0) {
                row.add(i)
                col.add(j)
            }
        }
    }
    for (let i of row){
        matrix[i]=new Array(n).fill(0);
    }
    for (let j of col){
        for (let i=0;i<m;i++){
            matrix[i][j]=0
        }
    }
};
