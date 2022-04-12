import { Editor } from "@tiptap/core";
import StarterKit from "@tiptap/starter-kit";

const editorElement = document.querySelector(".postContent");

console.log(editorElement.dataset.postContent);

new Editor({
  content: editorElement.dataset.postContent,
  element: editorElement,
  extensions: [StarterKit],
  editable: false,
  injectCSS: false,
});
