let names = new Set();
let productImages = new Set();
let basketImages = new Set();
let productCountInBasket = {};

document.getElementById("upload-button").addEventListener("click", openUploadScreen);
document.getElementById("cancel-button").addEventListener("click", closeUploadScreen);
document.getElementById("save-button").addEventListener("click", uploadProduct);
document.getElementById("put-button").addEventListener("click", putProduct);
document.getElementById("delete-button").addEventListener("click", deleteFromBasket);

function openUploadScreen(event) {
    document.getElementById("upload-screen").style.display = "block";
}

function closeUploadScreen(event) {
    document.getElementById("upload-screen").style.display = "none";
}

function uploadProduct(event) {
    const image = "./images/"+extractFilename(document.getElementById("product-image").value);
    const name = document.getElementById("product-name").value;
    const price = document.getElementById("product-price").value;
    const count = document.getElementById("product-count").value;
    const imageOk = imageFine(image);
    const nameOk = nameFine(name);
    const priceOk = priceFine(price);
    const countOk = countFine(count);
    if(imageOk&&nameOk&&priceOk&&countOk) {
        const productList = document.getElementById("product-list");
        const table = document.createElement("table");
        const div = document.createElement("div");
        table.setAttribute("class", "product");
        table.setAttribute("id", name+"-product");
        div.setAttribute("class", "product-div");
        table.appendChild(createRow(createUncheckedCheckboxNode()));
        table.appendChild(createRow(createImageNode(image)));
        table.appendChild(createTextRow(name));
        table.appendChild(createTextRow(price+"원"));
        table.appendChild(createBuyCountRow());
        table.appendChild(createTextRow("합계 "+price+"원"));
        table.appendChild(createTextRow("총 "+count+"개 남음"));
        div.appendChild(table);
        productList.appendChild(div);
        productImages.add(image);
        closeUploadScreen();
    }
}

function putProduct(event) {
    const tbody = document.getElementById("basket-table-body");
    if(tbody.children) {
        const checkAll = document.getElementById("check-all");
        const node = createCheckedCheckboxNode();
        node.setAttribute("id", "check-all");
        node.addEventListener("click", checkAllChanged);
        checkAll.parentNode.replaceChild(node, checkAll);
    }
    productList = document.getElementsByClassName("product");
    for(let i=0; i<productList.length; i++) {
        const col = productList[i].children;
        if(col[0].firstChild.firstChild.checked) {
            const image = col[1].firstChild.firstChild.src;
            if(basketImages.has(image)) {
                const name = col[2].firstChild.firstChild.data;
                const buyCount = col[4].firstChild.firstChild.value;
                updateBasket(name, buyCount);
            }
            else {
                const row = fetchProduct(productList[i]);
                tbody.appendChild(row);
                basketImages.add(image);
            }
        }
    }
    calculateTotalCost();
}

function updateBasket(name, buyCount, event) {
    if(event) {
        const row = event.currentTarget.parentNode.parentNode;
        const name = row.children[2].firstChild.data;
        const prevCount = productCountInBasket[name];
        const price = row.children[3].firstChild.data;
        const buyCount = row.children[4].firstChild.value;
        row.replaceChild(createData(document.createTextNode((price * buyCount)+"원")), row.lastChild);
        productCountInBasket[name] = buyCount;
        updateProduct(name+"-product", buyCount - prevCount);
        calculateTotalCost();
    }
    else {
        const row = document.getElementById(name+"-basket");
        const prevCount = productCountInBasket[name];
        const newCount = parseInt(prevCount) + parseInt(buyCount);
        const price = row.children[3].firstChild.data;
        row.children[4].firstChild.value = newCount;
        row.replaceChild(createData(document.createTextNode((price * newCount)+"원")), row.lastChild);
        productCountInBasket[name] = newCount;
        updateProduct(name+"-product", buyCount);
    }
}

function deleteFromBasket() {
    const rows = document.getElementById("basket-table-body").children;
    for(let i=0; i<rows.length; i++) {
        if(rows[i].firstChild.firstChild.checked) {
            const id = rows[i].children[2].firstChild.data + "-product";
            const buyCount = rows[i].children[4].firstChild.value;
            const image = rows[i].children[1].firstChild.src;
            const name = rows[i].children[2].firstChild.data;
            delete productCountInBasket[name];
            basketImages.delete(image);
            updateProduct(id, -buyCount);
            rows[i].parentNode.removeChild(rows[i]);
            i--;
        }
    }
    calculateTotalCost();
}

function updateProduct(id, buyCount) {
    const product = document.getElementById(id);
    const stockAfter = parseInt(product.lastChild.firstChild.firstChild.data.split(" ")[1]) - buyCount;
    product.replaceChild(createTextRow("총 "+stockAfter+"개 남음"), product.lastChild)
}

function fetchProduct(product) {
    const col = product.children;
    const image = col[1].firstChild.firstChild.src;
    const name = col[2].firstChild.firstChild.data;
    const price = parseInt(col[3].firstChild.firstChild.data);
    const buyCount = col[4].firstChild.firstChild.value;
    const row = document.createElement("tr");
    row.setAttribute("id", name+"-basket");
    const checkboxNode = createCheckedCheckboxNode();
    checkboxNode.addEventListener("click", checkOrUncheck);
    row.appendChild(createData(checkboxNode));
    row.appendChild(createData(createImageNode(image)));
    row.appendChild(createData(document.createTextNode(name)));
    row.appendChild(createData(document.createTextNode(price)));
    row.appendChild(createBuyCountData(buyCount));
    row.appendChild(createData(document.createTextNode((price * buyCount)+"원")));
    updateProduct(name+"-product", buyCount);
    productCountInBasket[name] = buyCount;
    return row;
}

function calculateTotalCost() {
    const rows = document.getElementById("basket-table-body").children;
    const totalCost = document.getElementById("total-cost");
    const th = document.createElement("th");
    let sum = 0
    for(let i=0; i<rows.length; i++) {
        if(rows[i].firstChild.firstChild.checked) {
            sum += parseInt(rows[i].lastChild.firstChild.data);
        }
    }
    th.appendChild(document.createTextNode(sum));
    th.setAttribute("id", "total-cost");
    totalCost.parentNode.replaceChild(th, totalCost);
}

function calculateCostToBuy(event) {
    const target = event.currentTarget.parentNode.parentNode.nextSibling.firstChild;
    const buyCount = parseInt(event.currentTarget.value);
    const price = parseInt(event.currentTarget.parentNode.parentNode.previousSibling.firstChild.firstChild.data);
    const newCost = document.createTextNode("합계 "+(price * buyCount)+"원");
    target.replaceChild(newCost, target.firstChild);
}

function checkOrUncheck() {
    const rows = document.getElementById("basket-table-body").children;
    const checkAll = document.getElementById("check-all");
    const node = createUncheckedCheckboxNode();
    node.setAttribute("id", "check-all");
    node.addEventListener("click", checkAllChanged);
    for(let i=0; i<rows.length; i++) {
        if(!rows[i].firstChild.firstChild.checked) {
            if(checkAll.checked) {
                checkAll.parentNode.replaceChild(node, checkAll);
            }
            calculateTotalCost();
            return;
        }
    }
    if(!checkAll.checked) {
        node.setAttribute("checked", true);
        checkAll.parentNode.replaceChild(node, checkAll);
    }
    calculateTotalCost();
}

function checkAllChanged() {
    const rows = document.getElementById("basket-table-body").children;
    const checkAll = document.getElementById("check-all");
    if(checkAll.checked) {
        for(let i=0; i<rows.length; i++) {
            const node = createCheckedCheckboxNode();
            node.addEventListener("click", checkOrUncheck);
            rows[i].firstChild.replaceChild(node, rows[i].firstChild.firstChild);
        }
    }
    else {
        for(let i=0; i<rows.length; i++) {
            const node = createUncheckedCheckboxNode();
            node.addEventListener("click", checkOrUncheck);
            rows[i].firstChild.replaceChild(node, rows[i].firstChild.firstChild);
        }
    }
    calculateTotalCost();
}

function createUncheckedCheckboxNode() {
    const node = document.createElement("input");
    node.setAttribute("type", "checkbox");
    return node;
}

function createCheckedCheckboxNode() {
    const node = document.createElement("input");
    node.setAttribute("type", "checkbox");
    node.setAttribute("checked", true);
    return node;
}

function createImageNode(image) {
    const node = document.createElement("img");
    node.setAttribute("src", image);
    return node;
}

function createTextRow(text) {
    return createRow(document.createTextNode(text));
}

function createBuyCountRow() {
    const row = document.createElement("tr");
    const data = document.createElement("td");
    const node = document.createElement("input");
    node.setAttribute("type", "text");
    node.setAttribute("size", "5");
    node.addEventListener("keyup", calculateCostToBuy);
    node.value = 1;
    data.appendChild(node);
    data.appendChild(document.createTextNode(" 개"));
    row.appendChild(data);
    return row;
}

function createBuyCountData(buyCount) {
    const data = document.createElement("td");
    const input = document.createElement("input");
    const button = document.createElement("button");
    input.setAttribute("type", "text");
    input.value = buyCount;
    button.addEventListener("click", function(event){updateBasket("name",0,event)});
    button.appendChild(document.createTextNode("변경"));
    data.appendChild(input);
    data.appendChild(button);
    return data;
}

function createRow(node) {
    const tr = document.createElement("tr");
    const td = document.createElement("td");
    td.appendChild(node);
    tr.appendChild(td);
    return tr;
}

function createData(node) {
    const td = document.createElement("td");
    td.appendChild(node);
    return td;
}

function imageFine(image) {
    if(image === "./images/") {
        alert("상품 이미지를 추가하시오.");
        return false;
    }
    fileExtension = image.split(".")[2];
    if(fileExtension != "jpg" && fileExtension != "png" && fileExtension != "jpeg") {
        alert("이미지 파일이 아닙니다. ‘jpg’, ‘jpeg’ 또는 ‘png’을 확장자 로 가진 파일을 추가하시오.");
        return false;
    }
    if(productImages.has(image)) {
        alert("등록된 상품이 이미 있습니다.");
        return false;
    }
    return true;
}

function nameFine(name) {
    if(!name) {
        alert("상품 이름을 입력하시오.");
    return false;
    }
    if(names.has(name)) {
        alert("등록된 상품이 이미 있습니다.");
        return false;
    }
    if(!isNaN(name)) {
        alert("문자로 된 상품 이름을 입력하시오.");
        return false;
    }
    return true;
}

function priceFine(price) {
    if(!price) {
        alert("상품 가격을 입력하시오.");
        return false;
    }
    if(isNaN(price)) {
        alert("상품 가격에 숫자를 입력하시오.");
        return false;
    }
    if(price < 100) {
        alert("상품 가격을 100원 이상으로 입력하시오.");
        return false;
    }
    return true;
}

function countFine(count) {
    if(!count) {
        alert("상품 개수를 입력하시오.");
        return false;
    }
    if(isNaN(count)) {
        alert("상품 개수에 숫자를 입력하시오.");
        return false;
    }
    if(count > 100) {
        alert("최대 100개 이하로 입력하시오.");
        return false;
    }
    return true;
}

function extractFilename(path) {
  if (path.substr(0, 12) == "C:\\fakepath\\")
    return path.substr(12); // modern browser
  var x;
  x = path.lastIndexOf('/');
  if (x >= 0) // Unix-based path
    return path.substr(x+1);
  x = path.lastIndexOf('\\');
  if (x >= 0) // Windows-based path
    return path.substr(x+1);
  return path; // just the filename
}
