function getPrintmonStatus()
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
        	var timestamp = xmlHttp.responseText;
        	var date =timeConverter(timestamp);
            document.getElementById("last-printmon-update").innerHTML = date;        	
        }
    }
    xmlHttp.open("GET", 'http://nix.svt.ntnu.no:8080/last_update', true); // true for asynchronous 
    xmlHttp.send(null);
}

function timeConverter(UNIX_timestamp){
  var a = new Date(UNIX_timestamp * 1000);
  var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var year = a.getFullYear();
  var month = months[a.getMonth()];
  var date = a.getDate();
  var hour = a.getHours();
  var min = a.getMinutes();
  var sec = a.getSeconds();
  var time = date + ' ' + month + ' ' + year + ' ' + hour + ':' + min + ':' + sec ;
  return time;
}
getPrintmonStatus();
var id = setInterval('getPrintmonStatus();', 60000);