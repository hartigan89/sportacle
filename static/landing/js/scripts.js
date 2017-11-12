$(document).ready(function () {
   $("#pass1, #pass2").keyup(validate);
});


function validate() {
  var password1 = $("#pass1").val();
  var password2 = $("#pass2").val();

    if(password1 == password2) {
        document.getElementById("signup").disabled = false;
    }
    else {
        document.getElementById("signup").disabled = true;
    }
    
}




