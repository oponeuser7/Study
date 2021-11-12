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
    $("#search").click(function(event) {
        $("#result-area").empty();
        const input = $("#input").val();
        $.get("searchBook.php", {data:input}, function(data){
            if(data) {
                const table = $("<table></table>").append($("<tr><th>선택</th><th>제목</th><th>저자</th><th>출판년월일</th><th>출판사</th><th>화일</th><th>대출여부</th></tr>"));
                const books = JSON.parse(data);
                for(const key in books) {
                    const book = books[key];
                    const checkbox = $("<td></td>").append($("<input>").attr("type", "checkbox"));
                    const title = $("<td></td>").addClass("book-name").text(book.title);
                    const authors = $("<td></td>").text(book.authors.toString());
                    const publishDate = $("<td></td>").text(book.publishDate);
                    const publisher = $("<td></td>").text(book.publisher);
                    const file = $("<td></td>").append($("<a>미리보기</a>").attr("href", "http://localhost:8888/WP07/HW2/uploads/"+book.fileName).attr("target", "_blank"));
                    const rental = $("<td></td>").addClass("rental").text(book.rental);
                    table.append($("<tr></tr>").addClass("search-row").append(checkbox, title, authors, publishDate, publisher, file, rental));
                }
                $("#result-area").append(table);
                const rentButton = $("<button>대출하기</button>").attr("type","button");
                rentButton.click(function(event) {
                    $.post("identification.php", {}, function(data) {
                        if(data=="success") {
                            const rows = $(".search-row");
                            let noRentedBookSelected = true;
                            rows.each(function() {
                                const checked = $(this).find("input").is(":checked");
                                const rental = $(this).find(".rental").text();
                                if(checked && rental=="rented") {
                                    noRentedBookSelected = false;
                                }
                            });
                            if(noRentedBookSelected) {
                                const bookNames = []
                                const rentalDates = []
                                rows.each(function() {
                                    const checked = $(this).find("input").is(":checked");
                                    console.log(checked);
                                    if(checked) {
                                        const rental = $(this).find(".rental");
                                        const temp = new Date();
                                        bookNames.push($(this).find(".book-name").text());
                                        rentalDates.push(temp.getFullYear()+'-'+(temp.getMonth()+1)+'-'+temp.getDate());
                                        rental.text("rented");
                                    }
                                });
                                console.log(bookNames);
                                console.log(rentalDates);
                                $.post("rentBook.php", {bookNames:bookNames, rentalDates:rentalDates}, function() {
                                    alert("대출되었습니다");
                                });
                            }
                            else alert("대출 가능한 도서만 선택해주세요");
                        }
                        else alert("로그인 후 대출 가능합니다");
                    });
                });
                $("#result-area").append($("<br>"), rentButton);
            }
        });
    });
});

function validate(id, password) {
    return /^([A-Za-z0-9]){6,15}$/.test(id) && /^.*(?=^.{8,15}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$/.test(password);
}