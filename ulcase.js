// ulcase library

function convertToUppercase(){const selectedText=getSelectedText();if(selectedText){replaceSelectedText(selectedText.toUpperCase());}}
function convertToLowercase(){const selectedText=getSelectedText();if(selectedText){replaceSelectedText(selectedText.toLowerCase());}}
function removeFormats(){const selectedText=getSelectedText();if(selectedText){replaceSelectedText(selectedText);}}
function getSelectedText(){if(window.getSelection){return window.getSelection().toString();}
return'';}
function replaceSelectedText(newText){const selection=window.getSelection();if(!selection.rangeCount)return;const range=selection.getRangeAt(0);range.deleteContents();range.insertNode(document.createTextNode(newText));}
document.addEventListener('keydown',function(event){if(event.altKey&&event.key==='u'){event.preventDefault();convertToUppercase();}});document.addEventListener('keydown',function(event){if(event.altKey&&event.key==='l'){event.preventDefault();convertToLowercase();}});document.addEventListener('keydown',function(event){if(event.altKey&&event.key===';'){event.preventDefault();removeFormats();}});
