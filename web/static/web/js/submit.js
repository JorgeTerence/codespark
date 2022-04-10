import { Editor } from "@tiptap/core";
import StarterKit from '@tiptap/starter-kit';

new Editor({
  element: document.querySelector(".editor"),
  extensions: [StarterKit],
  injectCSS: false,
});

document.getElementById("submit").addEventListener('click', () => {

});
