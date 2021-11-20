const infoArray = [];

function StudentInfo(n, k, m, e) {
    this.name = n;
    this.korean = parseInt(k);
    this.math = parseInt(m);
    this.english = parseInt(e);
}

StudentInfo.prototype.sum = function(koreanChecked, mathChecked, englishChecked) {
    let acc = 0;
    if(koreanChecked) {
        acc += this.korean;
    }

    if(mathChecked) {
        acc += this.math;
    }

    if(englishChecked) {
        acc += this.english;
    }

    return acc;
}

$("document").ready(function() {
    $("#save").click(function() {
        const name = $("#name").val();
        const korean = $("#korean").val();
        const math = $("#math").val();
        const english = $("#english").val();
        infoArray.push(new StudentInfo(name, korean, math, english));
        alert(infoArray.length+"개의 학생정보가 저장되었습니다.");
    });

    $("#search").click(function() {
        $("#search-result").empty();
        for(const student of infoArray) {
            console.log(student);
            const name = student.name;
            const kchecked = $("#korean-check").is(":checked");
            const mchecked = $("#math-check").is(":checked");
            const echecked = $("#english-check").is(":checked");
            const sum = student.sum(kchecked, mchecked, echecked);
            $("#search-result").append(`<li>${name} : ${sum}</li>`);
        }
    });
});

