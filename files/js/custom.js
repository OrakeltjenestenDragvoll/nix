function getPrintmonStatus()
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            document.getElementById("last-printmon-update").innerHTML = xmlHttp.responseText;;
        }
    }
    xmlHttp.open("GET", 'https://nix.orakel.ntnu.no:8443/last_update', true); // true for asynchronous
    xmlHttp.send(null);
}

getPrintmonStatus();
var id = setInterval('getPrintmonStatus();', 60000);