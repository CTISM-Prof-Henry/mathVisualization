

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