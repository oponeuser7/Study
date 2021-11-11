$(document).ready(function() {
    $.post("identification.php", {}, function(data) {
        if(data=="success") {
            const button = $("<button>로그아웃</button>");
            button.attr("type", "button");
            button.attr("id", "sign-out");
            button.click(function(event) {
                $.post("signOut.php", {}, function() {
                    const button = $("<button>로그인</button>");
                    button.attr("type", "button");
                    button.attr("id", "sign-in");
                    button.click(function(event) {
                        $("#sign-in-screen").toggle();
                    });
                    $("#sign-out").remove();
                    $("#user-area").prepend(button);
                });
            });
            $("#sign-in").remove();
            $("#user-area").prepend(button);
        }
    });
    $("#sign-in").click(function(event) {
        $("#sign-in-screen").toggle();
    });
    $("#submit-button").click(function(event) {
        const id = $("#id").val();
        const password = $("#password").val();
        if(validate(id, password)) {
            $.post("signIn.php", {id:id, password:password}, function(data) {
                if(data=="success") {
                    const button = $("<button>로그아웃</button>");
                    button.attr("type", "button");
                    button.attr("id", "sign-out");
                    button.click(function(event) {
                        $.post("signOut.php", {}, function() {
                            const button = $("<button>로그인</button>");
                            button.attr("type", "button");
                            button.attr("id", "sign-in");
                            button.click(function(event) {
                                $("#sign-in-screen").toggle();
                            });
                            $("#sign-out").remove();
                            $("#user-area").prepend(button);
                        });
                    });
                    $("#sign-in").remove();
                    $("#user-area").prepend(button);
                    $("#sign-in-screen").hide();
                    $("#id").val("");
                    $("#password").val("");
                }
                else alert("아이디 또는 패스워드가 틀렸습니다");        
            });
        }
        else alert("아이디 또는 패스워드의 입력 양식을 체크해주세요");
    });
    $("#sign-up-button").click(function(event) {
        const id = $("#id").val();
        const password = $("#password").val();
        if(validate(id, password)) {
            $.post("signUp.php", {id:id, password:password}, function(data) {
                alert("회원가입이 완료되었습니다");
            });
        }
        else alert("아이디 또는 패스워드의 입력 양식을 체크해주세요");
    });
    $("#rent-info").click(function(event) {

    });
});

function validate(id, password) {
    return /^([A-Za-z0-9]){6,15}$/.test(id) && /^.*(?=^.{8,15}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$/.test(password);
}