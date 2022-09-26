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

        document.getElementById("mouse_position").textContent = "Mouse position: (" + event.pageX + ", " + event.pageY + ")";
    }
})();

(function () {
    document.onmousedown = handleMouseDown;

    function handleMouseDown(event) {
        document.getElementById("mouse_click").textContent = "Mouse click? True";
    }
})();

(function () {
    document.onmouseup = handleMouseUp;

    function handleMouseUp(event) {
        document.getElementById("mouse_click").textContent = "Mouse click? False";
    }
})();

//

// modais
let start_session_modal = document.getElementById("start_session_modal");
let finish_session_modal = document.getElementById("finish_session_modal");

// botões que abrem os modais
let button_finish_session = document.getElementById("button_finish_session");
let button_start_session = document.getElementById("button_start_session");

// spans que fecham os modais (botão x)
let span_start_session_modal = document.getElementById("span_start_session_modal");
let span_finish_session_modal = document.getElementById("span_finish_session_modal");

// começa com o modal de instruções/início da sessão aberto
span_start_session_modal.style.display = "block";
start_session_modal.style.display = "block";

// quando o usuário clicar no botão de finalizar sessão, abre modal com resultados
button_finish_session.onclick = function() {
  finish_session_modal.style.display = "block";
}

// quando o usuário clicar no botão de iniciar sessão (dentro do modal),
// fecha o modal
button_start_session.onclick = function() {
  span_start_session_modal.style.display = "none";
  start_session_modal.style.display = "none";
}

// quando o usuário apertar o x do span dentro do modal, fecha-o
span_start_session_modal.onclick = function() {
  span_start_session_modal.style.display = "none";
  start_session_modal.style.display = "none";
}

// quando o usuário apertar o x do span dentro do modal, fecha-o
span_finish_session_modal.onclick = function() {
  span_finish_session_modal.style.display = "none";
  finish_session_modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
// window.onclick = function(event) {
//   if (event.target === session_modal) {
//     session_modal.style.display = "none";
//   }
// }