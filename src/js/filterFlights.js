
function ajaxGetRequest(path){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            console.log(this.response);
        }
    };
    request.open("GET", path);
    request.send();
}

function filterFlights(path){
    let location = document.getElementById("location").value;
    let price = document.getElementById("price").value;
    let currencyType = document.getElementById("currencyType").value;
    let startdate = document.getElementById("startdate").value;
    let enddate = document.getElementById("enddate").value;
    userInput = [location, price, currencyType, startdate, enddate];
    convertUserInput(userInput);


    //Security needed here
}

function convertUserInput(param){

}

