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

// Get the modal
let modal = document.getElementById("session_window");

// Get the button that opens the modal
let btn = document.getElementById("button_new_session");

// Get the <span> element that closes the modal
let span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target === modal) {
    modal.style.display = "none";
  }
}