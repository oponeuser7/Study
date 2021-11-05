$(document).ready(function() {
    $("#read-button").click(function() {
        if(localStorage.length==0){
        alert("저장된 계획이 없습니다.");
        }
        else {
            for(let i =0; i < localStorage.length; i++){
                const text = localStorage.key(i);
                const div = localStorage.getItem(text);
                const todo = document.createElement("div");
                todo.setAttribute("draggable", "true");
                todo.setAttribute("id", text);
                todo.setAttribute("class", "to-do");
                todo.setAttribute("contenteditable", "true");
                todo.appendChild(document.createTextNode(text));
                todo.addEventListener("dragstart", function(ev) {
                    ev.dataTransfer.setData("text", ev.target.id);
                });
                todo.addEventListener("keyup", function(ev) {
                    const div = $(this).parent().attr("id");
                    const text = $(this).text();
                    localStorage.removeItem(ev.currentTarget.id);
                    $(this).attr("id", text);
                    localStorage.setItem(text, div); 
            });
                $("#"+div).append(todo); 
            }
        }
    });
    $("#clear-button").click(function() {
        localStorage.clear();
        $("#today").empty();
        $("#tomorrow").empty();
    });
    $("#append-button").click(function() {
        const input = $("#data").val();
        if(input) {
            const todo = document.createElement("div");
            todo.setAttribute("draggable", "true");
            todo.setAttribute("id", input);
            todo.setAttribute("class", "to-do");
            todo.setAttribute("contenteditable", "true");
            todo.appendChild(document.createTextNode(input));
            todo.addEventListener("dragstart", function(ev) {
                ev.dataTransfer.setData("text", ev.target.id);
            });
            todo.addEventListener("keyup", function(ev) {
                const div = $(this).parent().attr("id");
                const text = $(this).text();
                localStorage.removeItem(ev.currentTarget.id);
                $(this).attr("id", text);
                localStorage.setItem(text, div);
            });
            document.getElementById("to-do-box").appendChild(todo);
            $("#data").val();
        }
    });
});
document.getElementById("today").addEventListener("drop", function(ev) {
    ev.preventDefault();
    const data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
    localStorage.setItem(data, ev.target.id); 
});
document.getElementById("today").addEventListener("dragover", function(ev) {
    ev.preventDefault(); 
});
document.getElementById("tomorrow").addEventListener("drop", function(ev) {
    ev.preventDefault();
    const data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
    localStorage.setItem(data, ev.target.id); 
});
document.getElementById("tomorrow").addEventListener("dragover", function(ev) {
    ev.preventDefault(); 
});