// thanks to https://stackoverflow.com/a/7790764/2202739 for allowing this code to run!

const timer = 300000; // 5 minutos (em milisegundos)
// const timer = 5000; // 5 segundos

let start = new Date().getTime();
let running = false;
let finish_collecting_data_timeout = null;

let collected_data;

function record_mouse_movement() {
    if(running) {
        let data =
            '"' + new Date().getTime() + '",' +
            '"' + document.getElementById("mouse_position_value").textContent + '",' +
            '"' + document.getElementById("mouse_click_value").textContent + '"\n';

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
    let minutes;
    let seconds;
    if(seconds_timer < 0) {
        minutes = '00';
        seconds = '00';
    } else {
        minutes = parseInt(seconds_timer / 60);
        seconds = parseInt(seconds_timer % 60);

        if((minutes.toString().length) === 1) {
            minutes = '0' + minutes;
        }
        if(seconds.toString().length === 1) {
            seconds = '0' + seconds;
        }
    }

    let countdown_timer = document.getElementById("countdown_timer");
    countdown_timer.textContent = "Tempo restante: " + minutes + ":" + seconds;
}

function format_time_file(time) {
    return time.getHours() + '-' + time.getMinutes() + '-' + time.getSeconds() + ' ' +
        time.getDay() + '-' + time.getMonth() + '-' + time.getFullYear()
}

// TODO revisar
function finish_session_func_show() {
    running = false;

    if(finish_collecting_data_timeout !== null) {
        clearTimeout(finish_collecting_data_timeout);
        finish_collecting_data_timeout = null;
    }

    let now = new Date();
    let filename = 'tracking_' + format_time_file(now) + ".csv";

    let myFile = new File(collected_data, filename, {type: "text/plain;charset=utf-8"});
    saveAs(myFile);
    console.log('arquivo com informações do mouse salvo com sucesso!');
}

// TODO revisar
function start_session_func_close() {
    start = new Date().getTime();
    running = true;
    collected_data = Array('"miliseconds","mouse_position","mouse_click"\n');

    finish_collecting_data_timeout = setTimeout(finish_collecting_data, timer);
}

let registered_callbacks = false;

function finish_collecting_data() {
    try {
        // se o modal de finalização da sessão não estiver aberto, clica no botão que finaliza
        // lançará um erro, pois pelo dash o modal não está presente na página até ser clicado
        let finish_session_modal = document.getElementById('finish_session_modal');
        console.log('finish_session_modal localizado');
        if(finish_session_modal.hidden) {
            console.log('finish_session_modal localizado e está oculto');
            document.getElementById('button_finish_session').click();
        }

    } catch (error) {
        document.getElementById('button_finish_session').click();
        console.log('finish_session_modal está fechado');
    }
}

function registerCallbacks() {
    // if(!registered_callbacks) {
    try {
        document.getElementById('button_start_session').onclick = start_session_func_close;
        document.getElementById('close_finish_session_modal').onclick = start_session_func_close;
        document.getElementById('button_finish_session').onclick = finish_session_func_show;

        registered_callbacks = true;

        console.log('callbacks registradas com sucesso!');
    } catch (error) {
        // does nothing
    }
    // }
}

window.setInterval(registerCallbacks, 50);  // a cada 10 milisegundos
window.setInterval(update_countdown_timer, 1000);  // a cada segundo
window.setInterval(record_mouse_movement, 50);  // a cada 50 milisegundos
