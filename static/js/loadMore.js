const list = document.querySelector(".content1");
// const listItems = list.querySelectorAll(".card");
const ajaxLoadMoreBtn = document.querySelector(".ajax-load-more");

let k = 21;
let j = 40;

ajaxLoadMoreBtn.addEventListener("click", function () {
  let range = `.card:nth-child(n+${k}):nth-child(-n+${j})`;
  list
    .querySelectorAll(range)
    .forEach((elem) => (elem.style.display = "block"));

  if (900 <= j) {
    this.remove();
  } else {
    k += 20;
    j += 20;
  }
});
