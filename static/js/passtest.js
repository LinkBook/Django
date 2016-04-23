/**
 * Created by HamZare on 23/04/2016.
 */
function checkPass() {
    //Store the password field objects into variables ...
    var pass1 = document.getElementById('id_password');
    var pass2 = document.getElementById('id_repassword');
    //Store the Confimation Message Object ...
    var message = document.getElementById('confirmMessage');
    //Set the colors we will be using ...
    var goodColor = "#66cc55";
    var badColor = "#ff6655";
    //Compare the values in the password field
    //and the confirmation field
    if (pass1.value == pass2.value) {
        //The passwords match.
        //Set the color to the good color and inform
        //the user that they have entered the correct password
        pass2.style.backgroundColor = goodColor;
        message.style.color = goodColor;
        message.className = "glyphicon glyphicon-ok";
        //message.innerHTML = "حله (: بزن ثبت نام رو ..."
    } else {
        //The passwords do not match.
        //Set the color to the bad color and
        //notify the user.
        pass2.style.backgroundColor = badColor;
        message.style.color = badColor;
        message.className = "glyphicon glyphicon-remove";
        //message.innerHTML = "رمزا رو یکسان وارد کن تا کام روا شی ... ):"
    }
}


function Validate() {
    var password = document.getElementById("id_password").value;
    var confirmPassword = document.getElementById("id_repassword").value;
    if (password != confirmPassword) {
        alert("Passwords do not match.");
        return false;
    }
    return true;
}