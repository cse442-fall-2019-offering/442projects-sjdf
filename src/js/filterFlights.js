
function ajaxGetRequest(path){
    var request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            console.log(this.response);
        }
    };
    request.open("GET", path);
    request.send();
}

function filterFlights(path){
    var location = document.getElementById("current_location").value;
    var price = document.getElementById("price").value;
    var currencyType = document.getElementById("currencyType").value;
    var startdate = document.getElementById("startdate").value;
    var enddate = document.getElementById("enddate").value;
    userInput = [location, price, currencyType, startdate, enddate];
    //convertUserInput(userInput);


    //Security needed here
}

function convertUserInput(param){

}

