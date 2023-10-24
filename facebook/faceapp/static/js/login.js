// function login(){
//      email=document.getElementById("email");
//      password=document.getElementById("password");

//     if(email.value==""){
//         // email.style.borderColor="red";
//         // alert("enter your email")
//         // email.focus();
//         // return false;
//     }
//     else{
//         return true;
//     }
// }

function signup(){
    firstname=document.getElementById("first");
    secondname=document.getElementById("second");
    Mobile=document.getElementById('mobile');
    email=document.getElementById('email');
    password=document.getElementById('pwd')
    day=document.getElementById('day');
    month=document.getElementById('month');
    year=document.getElementById('year');
    male=document.getElementById("male");
    female=document.getElementById("fem")
    if(firstname.value==""){
        firstname.style.borderColor="red";
        document.getElementById('firstname').innerHTML = "Enter your first name";
        firstname.focus();
        return false;
    }
    else if(secondname.value==""){
        secondname.style.borderColor="red";
        document.getElementById('lastname').innerHTML = "Enter your last name";
        secondname.focus();
        return false;
    }
    else if(Mobile.value == "" || isNaN(Mobile.value) ) {
        Mobile.style.borderColor = "red";
        document.getElementById('mob').innerHTML = "Enter your mobile number";
        Mobile.focus();
        return false;

    }
    else if( Mobile.value.length!=10){
        document.getElementById('mob').innerHTML = "Length should be 10";
        Mobile.focus();
        return false;
    }
    else if( email.value==""){
        document.getElementById('eml').innerHTML = "enter your email id";
        email.focus();
        return false;
    }
    else if(password.value==""){
        // password.style.borderColor="red";
        password.focus();
        document.getElementById('pass').innerHTML = "enter your password";
        return false;
    }
    else if(password.value.length < 8){
        // password.style.borderColor="red";
        password.focus();
        document.getElementById('pass').innerHTML = "length should be atlest 8";
        return false;
    }
    else if(day.value=="" || month.value=="" || year.value==""){
        // password.style.borderColor="red";
        day.focus();
        month.focus();
        year.focus()
        document.getElementById('er').innerHTML = "select date of birth";
        return false;
    }
    // else if(isNaN(day.value) || isNaN(year.value)){
    //     // password.style.borderColor="red";
    //     document.getElementById('er').innerHTML = "select date of birth";
    //     return false;
    // }
    else if(female.value="" && male.value==""){
        // password.style.borderColor="red";
        document.getElementById('gen').innerHTML = "select gender";
        return false;
    }
    else{
        return true
    }
}