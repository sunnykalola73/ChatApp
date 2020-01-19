function set_cookie(key, value, time) {
    var d = new Date();
    d.setTime(d.getTime() + (time * 1000));
    var expires = "expires=" + d.toUTCString();
    document.cookie = key + "=" + value + ";" + expires + ";path=/";
}


function delete_cookie(key) {
    document.cookie = key + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
}

function delete_all_cookie() {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var tmp = cookies[i].split('=');
        delete_cookie(tmp[0].trim());
    }
}

function logout() {
    window.location = '/logout';
}

function go(page) {
    window.location = '/room';
}

function pass_validator() {
    setInterval(function() {
        var ele = document.getElementById("password");
        var ele2 = document.getElementById("cpassword");
        var uname = document.getElementById("uname");
        var email = document.getElementById("email");
        // var msg = "*Password length should be 6-128<br>*should contain uppercase & lowercase alphabets, numbers & special characters";
        var err = "";
        if (uname.value == "") {
            err += "*Username can't be blank<br/>"
        }
        if (3 < uname.value.length < 33) {
            err += "";
        } else {
            err += "*Username length should be 4-32<br/>";
        }
        if (uname.value.match("^[A-Za-z][a-zA-Z0-9_]*")) {
            err += "";
        } else if (uname.value.charAt(0).match("[0-9_]")) {
            err += "username should start with alphabets only<br/>"
        } else {
            err += "*username should contain only numbers, alphabets and underscore<br/>";
        }
        if (ele.value == "") {
            err += "*password can't be blank<br/>";
        }
        if (ele.value.length > 5 && ele.value.length < 129) {
            console.log(ele.value.length);
            err += "";
        } else {
            err += "*Password length should be 6-128<br/>";
        }
        if (ele.value.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=[^\s].*[^\s])(?=.{6,129})")) {
            err += "";
        } else {
            err += "Password must contain one lowercase,one uppercase,one digit and one special character<br/>"
        }
        console.log(ele.value);
        if (ele.value != ele2.value) {
            err += "*Password doesn't match with confirm password<br/>";
        }
        // // if (email.match("/^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;")) {
        // //     err += "";
        // // } else {
        // //     err += "*Invalid Email<br/>";
        // // }
        // $("#email").val($("#email").val.toString().toLowerCase());
        $("#err").html(err);
        //  else {
        //     // $("#err").html("");
        //     $("#signup").removeAttr("disabled");
        //     console.log("match");
        // }
        if (err == "") {
            $("#signup").removeAttr("disabled");
        } else {
            $("#signup").attr("disabled", true);
        }
    }, 1000);
}

// $(document).ready(function() {
//     $("#password").blur(function() {
//         $("#err").val("Enter Details");
//         var passwd = $(this).val;
//         if (5 < passwd.length < 129) {
//             $("#err").html("*Password length should be 6-128 and should contain uppercase & lowercase alphabets, numbers & special characters");
//         } else {
//             $("#err").html("");
//         }
//     });
// });