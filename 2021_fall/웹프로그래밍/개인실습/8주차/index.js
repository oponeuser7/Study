$(document).ready(function() {
    $("#search-word").keyup(function() {
        const searchName = $(this).val();
        $("#results").empty();
        if(searchName) {
            $.get("searchByName.php", {name:searchName}, function(data) {
                const result = JSON.parse(data);
                for(key in result) {
                    const student = result[key];
                    const li = $("<li></li>");
                    const firstNode = $("<span></span>").addClass("major-button").text(student.major);
                    const secondNode = $("<span></span>").text(" , "+student.name);
                    const thirdNode = $("<div></div>").addClass("student-list").hide();
                    firstNode.click(function() {
                        const searchMajor = $(this).text();
                        const temp = $(this).next().next().empty();
                        $.get("searchByMajor.php", {major:searchMajor}, function(data) {
                            const result = JSON.parse(data);
                            for(key in result) {
                                const name = result[key].name;
                                const node = $("<p></p>").addClass("names").text(name);
                                temp.append(node);
                            }
                        });
                        temp.toggle();
                    });
                    li.append(firstNode, secondNode, thirdNode);
                    $("#results").append(li);
                }
            });
        }
    });
});