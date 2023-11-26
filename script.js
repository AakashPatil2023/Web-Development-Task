let option = document.getElementById("option")
let name = document.getElementById("name");
let email = document.getElementById("email");
let number = document.getElementById("number");
let pan = document.getElementById("pan");
let pin_code = document.getElementById("pincode");
let kyc = document.getElementById("kyc");
let file = document.getElementById("file");
let password = document.getElementById("password");
let confirmPassword = document.getElementById("confirmPassword");
let checkbox = document.getElementById("checkbox");

function formValidation() {
    
    if (option.value == "") {
        document.getElementById("optionError").innerHTML = "Please select option!";
        return false;
    }
    else if (name.value == "") {
        document.getElementById("userError").innerHTML = "Name is empty!";
        return false;
    }
    else if (email.value == "") {
        document.getElementById("mailError").innerHTML = "Email is empty!";
        return false;
    }
    else if (number.value == "") {
        document.getElementById("numError").innerHTML = "Number is empty!";
        return false;
    }
    else if (pan.value == "") {
        document.getElementById("panError").innerHTML = "Pan Number is empty!";
        return false;
    }
    else if (pincode.value == "") {
        document.getElementById("pinCodeError").innerHTML = "Pin Code is empty!";
        return false;
    }
    else if (kyc.value == "") {
        document.getElementById("kycError").innerHTML = "KYC Number is empty!";
        return false;
    }
    else if (!file.value) {
        document.getElementById("fileError").innerHTML = "Please Select the file!";
        return false;
    }
    else if (password.value == "") {
        document.getElementById("passError").innerHTML = "Password is empty!";
        return false;
    }
    else if(confirmPassword.value == "" || confirmPassword.value != password.value ){
        document.getElementById("conPassError").innerHTML = "Password is empty or does not match!";
        return false;
    }
    else if(checkbox.checked == false){
        document.getElementById("checkboxError").innerHTML = "Please check terms and condition!";
        return false;
    }
    else{
        return true; 
    }
       
}