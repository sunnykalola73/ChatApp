// $(document).ready(function() {
//     $("#password").blur(function() {
//         $("#err").val("Enter Details");
//         var passwd = $(this).val;
//         if (5 < passwd.length < 129) {
//             $("#err").html("*Password length should be 6-128");
//         } else {
//             $("#err").html("");
//         }
//         var passwd_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d.*)(?=.*\W.*)[a-zA-Z0-9\S]{8,15}$"
//         if (passwd.match(passwd_regex)) {
//             alert("success");
//         } else {
//             alert("Fail")
//         }
//     });
// });



function set_cookie(key, value, time) {
    var d = new Date();
    d.setTime(d.getTime() + (time * 1000));
    var expires = "expires=" + d.toUTCString();
    document.cookie = key + "=" + value + ";" + expires + ";path=/";
}

function get_cookie(key) {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var tmp = cookies[i].split('=');
        if (key == tmp[0].trim()) {
            return tmp[1].trim();
        }
    }
    return null;
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