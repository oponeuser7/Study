const images = '<img id="img1" src="./images/img1.jpg" draggable="true" ondragstart="drag(event)" /><img id="img2" src="./images/img2.jpg"  draggable="true" ondragstart="drag(event)" /><img id="img3" src="./images/img3.jpg"  draggable="true" ondragstart="drag(event)" />';

function readSession(ev) {
    if(sessionStorage.length==0){
        alert("바구니에 담겨 있는 이미지가 없습니다.");
    }
    else {
        for(let i =0; i < sessionStorage.length; i++){
            var img = sessionStorage.key(i);
            var value = sessionStorage.getItem(img);
            if(value =="div2"){
                document.getElementById("div2").appendChild(document.getElementById(img));
            } else {
                document.getElementById("div3").appendChild(document.getElementById(img));
            }
        }
    }
}

function clearSession(ev) {
    sessionStorage.clear();
    $("#div2").empty();
    $("#div3").empty();
    $("#image").empty().html(images);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("img");
    ev.target.appendChild(document.getElementById(data));
    if (typeof(Storage) !== "undefined") {
        sessionStorage.setItem(data, ev.target.id); 
    }
    else {
        alert ("서버가 웹 스토리지를 지원하지 않습니다.");
    }
}

function allowDrop(ev) {
        ev.preventDefault();
}
        
function drag(ev) {
    ev.dataTransfer.setData("img", ev.target.id);
}

