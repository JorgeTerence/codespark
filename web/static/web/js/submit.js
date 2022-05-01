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
const codeBtn = document.querySelector(".new-code");

codeBtn.addEventListener("click", () =>
  editor.chain().focus().toggleCodeBlock().run()
);

// TODO: check for a heading before sending and use that as a title
form.addEventListener("submit", (e) => {
  e.preventDefault();

  const editorJSONConent = editor.getJSON()?.content;

  const content = editor.getHTML();
  const subject = subjSelect.options.item(subjSelect.selectedIndex).value;
  const title = editorJSONConent[0]?.content[0]?.text;
  const peek = editorJSONConent[1]?.content[0]?.text;

  // TODO: Check for undefined

  fetch(form.action, {
    method: "POST",
    body: JSON.stringify({ content, subject, title, peek }),
    headers: { "X-CSRFToken": Cookies.get("csrftoken") },
  }).then((res) => (window.location.href = res.url));
});
