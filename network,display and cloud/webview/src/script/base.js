ctxT = document.getElementById('timer')
timer = ctxT.getContext("2d")

timer.beginPath()
timer.arc(105, 105, 110, 0, 2 * Math.PI)
timer.fillStyle = '#292929'
timer.fill()

timer.strokeStyle = '#18A0FB'
timer.lineWidth = 30
timer.beginPath()
timer.arc(105, 105, 100, 0, 1.5 * Math.PI);
timer.stroke();

sld = document.getElementById('canva_msk')
timer_txt = document.getElementById('timer_txt')

timer_txt.style.marginTop = 120 + 'px'
timer_txt.style.marginLeft = 95 + 'px'

document.getElementsByClassName('view')[0].style.width = window.innerWidth - 400 + 'px'
document.getElementsByClassName('view')[0].style.height=window.innerHeight  + 'px'

document.getElementById('iframe_view').src="view/src/webgl_loader_gcode.html"