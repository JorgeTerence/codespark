import { Editor } from "@tiptap/core";
import StarterKit from '@tiptap/starter-kit';

new Editor({
  element: document.querySelector(".editor"),
  extensions: [ StarterKit ],
  content: "<h1>Codespark Markdown Editor<h1>"
});
