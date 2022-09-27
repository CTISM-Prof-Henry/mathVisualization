// thanks to https://stackoverflow.com/a/7790764/2202739 for allowing this code to run!
(function() {
    document.onmousemove = handleMouseMove;
    function handleMouseMove(event) {
        let eventDoc, doc, body;

        event = event || window.event; // IE-ism

        // If pageX/Y aren't available and clientX/Y are,
        // calculate pageX/Y - logic taken from jQuery.
        // (This is to support old IE)
        if (event.pageX == null && event.clientX != null) {
            eventDoc = (event.target && event.target.ownerDocument) || document;
            doc = eventDoc.documentElement;
            body = eventDoc.body;

            event.pageX = event.clientX +
              (doc && doc.scrollLeft || body && body.scrollLeft || 0) -
              (doc && doc.clientLeft || body && body.clientLeft || 0);
            event.pageY = event.clientY +
              (doc && doc.scrollTop  || body && body.scrollTop  || 0) -
              (doc && doc.clientTop  || body && body.clientTop  || 0 );
        }

        document.getElementById("mouse_position_value").textContent = "(" + event.pageX + ", " + event.pageY + ")";
    }
})();

(function () {
    document.onmousedown = handleMouseDown;

    function handleMouseDown(event) {
        document.getElementById("mouse_click_value").textContent = "true";
    }
})();

(function () {
    document.onmouseup = handleMouseUp;

    function handleMouseUp(event) {
        document.getElementById("mouse_click_value").textContent = "false";
    }
})();

//

// modais
let start_session_modal = document.getElementById("start_session_modal");
let finish_session_modal = document.getElementById("finish_session_modal");

// botões que abrem os modais
let button_finish_session = document.getElementById("button_finish_session");
let button_start_session = document.getElementById("button_start_session");
let close_finish_session_modal = document.getElementById("close_finish_session_modal");

// spans que fecham os modais (botão x)
let span_start_session_modal = document.getElementById("span_start_session_modal");
let span_finish_session_modal = document.getElementById("span_finish_session_modal");

let timer = 300000; // 5 minutos (em milisegundos)
let start = new Date().getTime();
let running = false;

let countdown_timer = document.getElementById("countdown_timer");

let collected_data = Array('miliseconds,mouse_position,mouse_click\n');

function record_mouse_movement() {
    if(running) {
        let data = '"' + new Date().getTime() + '","' +
            document.getElementById("mouse_position_value").textContent + '","' +
            document.getElementById("mouse_click_value").textContent + '"\n';

        collected_data.push(data);
    }
}

function update_countdown_timer() {
    let seconds_timer;
    if(running) {
         seconds_timer = (timer - ((new Date().getTime()) - start)) / 1000;
    } else {
        seconds_timer = timer/1000;
    }
    let minutes = parseInt(seconds_timer / 60);
    let seconds = parseInt(seconds_timer % 60);

    if((minutes.toString().length) === 1) {
        minutes = '0' + minutes;
    }
    if(seconds.toString().length === 1) {
        seconds = '0' + seconds;
    }

    countdown_timer.textContent = "Tempo restante: " + minutes + ":" + seconds;
}

function format_time(time) {
    return time.getHours() + '-' + time.getMinutes() + '-' + time.getSeconds() + ' ' +
        time.getDay() + '-' + time.getMonth() + '-' + time.getFullYear()
}

function start_session_func_show() {
    span_start_session_modal.style.display = "block";
    start_session_modal.style.display = "block";
}

function finish_session_func_show() {
    finish_session_modal.style.display = "block";
    span_finish_session_modal.style.display = "block";

    running = false;

    let now = new Date();
    let filename = 'tracking_' + format_time(now) + ".csv";

    let myFile = new File(collected_data, filename, {type: "text/plain;charset=utf-8"});
    saveAs(myFile);
}

function start_session_func_close() {
    span_start_session_modal.style.display = "none";
    start_session_modal.style.display = "none";

    start = new Date().getTime();
    running = true;

    setTimeout(finish_session_func_show, timer);
}

function finish_session_func_close() {
    span_finish_session_modal.style.display = "none";
    finish_session_modal.style.display = "none";
}

function restart_session_func() {
    finish_session_func_close();
    start_session_func_show();
}

// começa com o modal de instruções/início da sessão aberto
start_session_func_show();
window.setInterval(update_countdown_timer, 1000);  // a cada segundo
window.setInterval(record_mouse_movement, 50);  // a cada 50 milisegundos

// quando o usuário apertar o x do span dentro do modal, fecha-o
span_start_session_modal.onclick = start_session_func_close;
// quando o usuário clicar no botão de iniciar sessão (dentro do modal),
// fecha o modal
button_start_session.onclick = start_session_func_close;

// quando o usuário clicar no botão de finalizar sessão, abre modal com resultados
button_finish_session.onclick = finish_session_func_show;

// quando o usuário apertar o botão de fechar dentro do modal, fecha-o
close_finish_session_modal.onclick = restart_session_func;
// quando o usuário apertar o x do span dentro do modal, fecha-o
span_finish_session_modal.onclick = restart_session_func;


// When the user clicks anywhere outside of the modal, close it
// window.onclick = function(event) {
//   if (event.target === session_modal) {
//     session_modal.style.display = "none";
//   }
// }