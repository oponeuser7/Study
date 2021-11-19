$(document).ready(function() {
    $("#add-author").click(function() {
        if($("#author-input").children().length<3){
            $("#author-input").append($('<input type="text" name="authors[]">'));
        }
    });
    $("#remove-author").click(function() {
        if($("#author-input").children().length>1){
            $("#author-input").children().last().remove();
        }
    });
});