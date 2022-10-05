// thanks to https://stackoverflow.com/a/7790764/2202739 for allowing this code to run!

let timer = 300000; // 5 minutos (em milisegundos)
let start = new Date().getTime();
let running = false;

let collected_data = Array('miliseconds,mouse_position,mouse_click\n');

function handleMouseMovement(event) {
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

function handleMouseDown(event) {
    document.getElementById("mouse_click_value").textContent = "true";
}

function handleMouseUp(event) {
    document.getElementById("mouse_click_value").textContent = "false";
}

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

    let countdown_timer = document.getElementById("countdown_timer");
    countdown_timer.textContent = "Tempo restante: " + minutes + ":" + seconds;
}

function format_time(time) {
    return time.getHours() + '-' + time.getMinutes() + '-' + time.getSeconds() + ' ' +
        time.getDay() + '-' + time.getMonth() + '-' + time.getFullYear()
}

function finish_session_func_show() {
    running = false;

    let now = new Date();
    let filename = 'tracking_' + format_time(now) + ".csv";

    document.getElementById('p_collected_data').textContent = collected_data;

    // let myFile = new File(collected_data, filename, {type: "text/plain;charset=utf-8"});
    // saveAs(myFile);
}

function start_session_func_close() {
    start = new Date().getTime();
    running = true;

    setTimeout(finish_session_func_show, timer);
}

document.onmousemove = handleMouseMovement;
document.onmousedown = handleMouseDown;
document.onmouseup = handleMouseUp;
window.setInterval(update_countdown_timer, 1000);  // a cada segundo
window.setInterval(record_mouse_movement, 50);  // a cada 50 milisegundos

let registered_callbacks = false;

function registerCallbacks() {
    if(!registered_callbacks) {
        try {
            document.getElementById('button_start_session').onclick = start_session_func_close;
            document.getElementById('close_finish_session_modal').onclick = start_session_func_close;
            document.getElementById('button_finish_session').onclick = finish_session_func_show;

            registered_callbacks = true;
        } catch (error) {
            // does nothing
        }
    }
}

window.setInterval(registerCallbacks, 1000);