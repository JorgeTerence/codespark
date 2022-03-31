const form = document.querySelector("form");
const addMarkdownBtn = document.getElementById("addMarkdown");
const addCodeBtn = document.getElementById("addCode");
const submitBtn = document.querySelector("input[type=submit]");

addMarkdownBtn.addEventListener("click", (event) => {
  event.preventDefault();
  const markdownBlock = document.createElement("textarea");
  markdownBlock.classList.add("markdown");
  form.appendChild(markdownBlock);
});

addCodeBtn.addEventListener("click", (event) => {
  event.preventDefault();
  const codeBlock = document.createElement("textarea");
  codeBlock.classList.add("code language-py");
  form.appendChild(codeBlock);
});
