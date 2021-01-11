var boxs = document.querySelectorAll(".box");

total = 0;

// 총 값 계산
boxs.forEach((el) => {
    console.log(el.getAttribute("value"));
    total += parseFloat(el.getAttribute("value"));
});

// width 지정
boxs.forEach((el) => {
    el.style.width = (parseFloat(el.getAttribute("value")) / total) * 100 + "%";
});
