function getPrintmonStatus()
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            document.getElementById("last-printmon-update").innerHTML = xmlHttp.responseText;;
        }
    }
    xmlHttp.open("GET", 'http://nix.svt.ntnu.no:8080/last_update', true); // true for asynchronous 
    xmlHttp.send(null);
}

getPrintmonStatus();
var id = setInterval('getPrintmonStatus();', 60000);