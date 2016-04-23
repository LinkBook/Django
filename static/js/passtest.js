/**
 * Created by HamZare on 23/04/2016.
 */
//Store the password field objects into variables ...
var password = document.getElementById("id_password")
    , confirm_password = document.getElementById("id_repassword");

//Store the Confimation Message Object ...
var message = document.getElementById('confirmMessage');

function checkPass() {
    //Set the colors we will be using ...
    var goodColor = "#66cc55";
    var badColor = "#ff6655";
    //Compare the values in the password field
    //and the confirmation field
    if (password.value == confirm_password.value) {
        //The passwords match.
        //Set the color to the good color and inform
        //the user that they have entered the correct password
        confirm_password.style.backgroundColor = goodColor;
        message.style.color = goodColor;
        message.className = "glyphicon glyphicon-ok";
        //message.innerHTML = "حله (: بزن ثبت نام رو ..."
    } else {
        //The passwords do not match.
        //Set the color to the bad color and
        //notify the user.
        confirm_password.style.backgroundColor = badColor;
        message.style.color = badColor;
        message.className = "glyphicon glyphicon-remove";
        //message.innerHTML = "رمزا رو یکسان وارد کن تا کام روا شی ... ):"
    }
}

/**
 * @return {boolean}
 */
function Validate() {
    //var password = document.getElementById("id_password").value;
    //var confirm_password = document.getElementById("id_repassword").value;
    if (password.value != confirm_password.value) {
        alert("Passwords do not match.");
        return false;
    }
    return true;
}


function validatePassword() {
    if (password.value != confirm_password.value) {
        confirm_password.setCustomValidity("Passwords Don't Match");
    } else {
        confirm_password.setCustomValidity('');
    }
}

password.onchange = validatePassword;
confirm_password.onmouseover = validatePassword;
confirm_password.onkeyup = checkPass;