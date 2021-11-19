$(document).ready(function() {
    $.get("getUserId.php", {}, function(data) {
        const userInfo = $("#user-info");
        const userName = $("<div></div").css("color", "blue").text(data);
        userInfo.append(userName).append($("<div>회원</div>"));
    });
    $.get("searchRent.php", {}, function(data) {
        if(data) {
            const table = $("<table></table>").append($("<tr><th>선택</th><th>책 제목</th><th>대출 날짜</th>"));
            const books = JSON.parse(data);
            for(const key in books) {
                const book = books[key];
                const checkbox = $("<td></td>").append($("<input>").attr("type", "checkbox"));
                const title = $("<td></td>").addClass("book-name").text(book.bookName);
                const rental = $("<td></td>").text(book.rental);
                table.append($("<tr></tr>").addClass("search-row").append(checkbox, title, rental));
            }
            $("#rent-list").append(table);
            const returnButton = $("<button>반납하기</button>").attr("type", "button");
            returnButton.click(function() {
                const rows = $(".search-row");
                const bookNames = [];
                rows.each(function() {
                    const checked = $(this).find("input").is(":checked");
                    if(checked) {
                        bookNames.push($(this).find(".book-name").text());
                        $(this).remove();
                    }
                });
                $.post("returnBook.php", {bookNames:bookNames}, function() {
                    alert("반환되었습니다");
                });
            });
            $("#rent-list").append($("<br>"), returnButton);
        }
    });
});