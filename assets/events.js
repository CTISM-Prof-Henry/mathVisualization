// thanks to https://stackoverflow.com/a/7790764/2202739 for allowing this code to run!

let timer = 300000; // 5 minutos (em milisegundos)
let start = new Date().getTime();
let running = false;

let collected_data;

function record_mouse_movement() {
    if(running) {
        let data = '"' + new Date().getTime() + '","' +
            document.getElementById("mouse_position_value").textContent + '","' +
            document.getElementById("mouse_click_value").textContent + '"';

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

// TODO revisar
function finish_session_func_show() {
    running = false;

    let now = new Date();
    let filename = 'tracking_' + format_time(now) + ".csv";

    let myFile = new File(collected_data, filename, {type: "text/plain;charset=utf-8"});
    saveAs(myFile);
    console.log('arquivo com informações do mouse salvo com sucesso!');
}

// TODO revisar
function start_session_func_close() {
    start = new Date().getTime();
    running = true;
    collected_data = Array('miliseconds,mouse_position,mouse_click');

    setTimeout(finish_session_func_show, timer);
}

let registered_callbacks = false;

function registerCallbacks() {
    if(!registered_callbacks) {
        try {
            document.getElementById('button_start_session').onclick = start_session_func_close;
            document.getElementById('close_finish_session_modal').onclick = start_session_func_close;
            document.getElementById('button_finish_session').onclick = finish_session_func_show;

            registered_callbacks = true;

            console.log('callbacks registradas com sucesso!');
        } catch (error) {
            // does nothing
        }
    }
}

window.setInterval(registerCallbacks, 10);  // a cada segundo
window.setInterval(update_countdown_timer, 1000);  // a cada segundo
window.setInterval(record_mouse_movement, 50);  // a cada 50 milisegundos
