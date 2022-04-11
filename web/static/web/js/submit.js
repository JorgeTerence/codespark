import { Editor } from "@tiptap/core";
import StarterKit from "@tiptap/starter-kit";
import Cookies from "js-cookie";

const editor = new Editor({
  element: document.querySelector(".editor"),
  extensions: [StarterKit],
  injectCSS: false,
});

const subjSelect = document.getElementsByName("subject").item(0);
const form = document.querySelector("form");

// TODO: check for a heading before sending and use that as a title
form.addEventListener("submit", (e) => {
  e.preventDefault();

  const editorJson = editor.getJSON();

  const content = editorJson?.content;
  const subject = subjSelect.options.item(subjSelect.selectedIndex).value;
  const title = content[0]?.content[0]?.text;

  fetch(form.action, {
    method: "POST",
    body: JSON.stringify({ content, subject, title }),
    headers: { "X-CSRFToken": Cookies.get("csrftoken") },
    redirect: "manual",
  })
    .then(res => res.text())
    .then(url => window.location = url);
});
