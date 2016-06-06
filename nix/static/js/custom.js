function sendMail() {
    var link = "mailto:me@example.com"
             + "?cc=myCCaddress@example.com"
             + "&subject=" + escape("This is my subject")
             + "&body=" + escape(document.getElementById("TEST")
    ;

    window.location.href = link;
}

setTimeout(function() {
    $("#message-list").children('.alert:first-child').fadeOut(1000);
}, 5000);