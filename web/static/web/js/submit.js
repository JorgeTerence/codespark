import { Editor } from "@tiptap/core";
import StarterKit from '@tiptap/starter-kit';

new Editor({
  element: document.querySelector(".editor"),
  extensions: [StarterKit],
  autofocus: true,
  injectCSS: false,
  content: "<h1>Compartilhe sua ideia! 💡<h1>",
});
