
// function draw(triangle){
// for(var i=0;i<triangle.points.length;i++){
//         drwa(triangle.points[i][0],triangle.points[i][1],triangle.points[i][3],triangle.points[i][4],triangle.points[i][6],triangle.points[i][7])
//         // drwa(triangle.points[i][0],triangle.points[i][2],triangle.points[i][3],triangle.points[i][5],triangle.points[i][6],triangle.points[i][8])
//     }
// }
function draw(tx,ty,tz,scl) {
    context.clearRect(0, 0, window.innerWidth, window.innerHeight);
    for (var i = 0; i < tx.length; i=i+3) {
        drwa(tx[i],ty[i],tx[i+1],ty[i+1],tx[i+2],ty[i+2],scl)
    }
}
function drwa(x1, y1, x2, y2, x3, y3, scl) {
    x1 = x1 *scl
    y1 = y1 *scl
    x2 = x2 *scl
    y2 = y2 *scl
    x3 = x3 *scl
    y3 = y3 *scl
    context.beginPath();
    context.moveTo(x1, y1);
    context.lineTo(x2, y2);
    context.lineTo(x3, y3);
    context.strokeStyle = '#ff0000'
    context.stroke();
    context.closePath();
    context.fillStyle = "rgb("+255+","+255+","+255+")";
    context.fill();
}