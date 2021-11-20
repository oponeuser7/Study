const infoArray = [];

function StudentInfo(n, k, m, e, major) {
    this.name = n;
    this.korean = parseInt(k);
    this.math = parseInt(m);
    this.english = parseInt(e);
    this.major = major;
}

StudentInfo.prototype.sum = function(koreanChecked, mathChecked, englishChecked) {
    let sum = 0;
    if(koreanChecked) sum += this.korean;
    if(mathChecked) sum += this.math;
    if(englishChecked) sum += this.english;
    return sum;
}

StudentInfo.prototype.avg = function(koreanChecked, mathChecked, englishChecked) {
    let sum = 0;
    let count = 0;
    if(koreanChecked) {
        sum += this.korean;
        count++;
    }
    if(mathChecked) {
        sum += this.math;
        count++;
    }
    if(englishChecked) {
        sum += this.english;
        count++;
    }
    return count>0 ? sum/count : 0;
}

$("document").ready(function() {
    $("#save").click(function() {
        const name = $("#name").val();
        const korean = $("#korean").val();
        const math = $("#math").val();
        const english = $("#english").val();
        const major = $("#major-input").val();
        infoArray.push(new StudentInfo(name, korean, math, english, major));
        alert(infoArray.length+"개의 학생정보가 저장되었습니다.");
    });

    $("#search").click(function() {
        $("#search-result").empty();
        const result = [];
        const major = $("#major-search").val();
        const order = $("#order").val();
        let overallAvg = 0;
        let count = 0;
        for(const student of infoArray) {
            if(major==="all" || student.major===major) {
                console.log("good");
                const name = student.name;
                const kchecked = $("#korean-check").is(":checked");
                const mchecked = $("#math-check").is(":checked");
                const echecked = $("#english-check").is(":checked");
                const sum = student.sum(kchecked, mchecked, echecked);
                const avg = student.avg(kchecked, mchecked, echecked);
                result.push([name,sum,avg]);
                overallAvg += avg;
                count++;
            }
        }
        if(order==="asc") result.sort((a, b) => a[1] - b[1]);
        else result.sort((a, b) => b[1] - a[1]);
        for(student of result) {
            $("#search-result").append(`<li>${student[0]}) 총점 : ${student[1]} | 평균점수 : ${student[2].toFixed(1)}</li>`);
        }
        overallAvg = count>0 ? (overallAvg/count).toFixed(2) : 0
        if(major==="all") $("#avg").text("모든 학과 평균 : "+overallAvg);
        else $("#avg").text("학과 평균 : "+overallAvg);
    });
});

