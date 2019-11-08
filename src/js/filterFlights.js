/**
 * @Author Javier Falca
 * @Last modified: 10/20/2019
 * @Description: Makes get requests with a specific path to url
 * @param string path to make a request to
 */
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
/**
 * @Author Javier Falca
 * @Last modified: 10/20/2019
 * @Description: Filters data based on user input
 * @param string path to make a request to
 */
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
/**
 * TODO: Convert user input into proper API parameters
 */
function convertUserInput(param){

}

/**
 * @Author Florebencia Fils-Aime
 * @Last modified: 11/3/2019
 * @Description: Create a JSON string out of the inputs and then do a post
 * request to that directory with AJAX.
 * @param
 */
//function sendFormDataToServer(){
//    var formData = JSON.stringify($("#userform").serializeArray());
//    console.log(formData);
//    var ajaxrequest = new XMLHttpRequest();
//    ajaxrequest.onreadystatechange = function(){
//        if (this.readyState === 4 && this.status === 200){
//            console.log(this.response);
//        }
//    };
//    ajaxrequest.open("POST", 'flights.html');
//    ajaxrequest.send(formData);
//    return true;
//}
