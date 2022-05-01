import Cookies from "js-cookie";

const voteBtns = document.getElementsByClassName("btn-vote");

for (const btn of voteBtns) {
  btn.addEventListener("click", () =>
    fetch(btn.dataset.voteUrl, {
      method: "POST",
      headers: { "X-CSRFToken": Cookies.get("csrftoken") },
    })
      .then(res => res.text())
      .then(votes => btn.parentNode.querySelector(".votes").innerHTML = votes)
    // .then(votes => btn.parentElement.querySelector(".votes").innerText = votes)
  );
}
