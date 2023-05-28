var draggableParagraph = document.getElementById('draggable-paragraph');
var initialFontSize = 16;

draggableParagraph.addEventListener('dragstart', dragStart);
draggableParagraph.addEventListener('dragend', dragEnd);

function dragStart(event) {
  event.dataTransfer.setData('text/plain', event.target.id);
  event.dataTransfer.effectAllowed = 'move';
  event.target.style.opacity = '0.5';
}

function dragEnd(event) {
  event.target.style.opacity = '1';
}

document.addEventListener('dragover', dragOver);
document.addEventListener('drop', drop);

function dragOver(event) {
  event.preventDefault();
}

function drop(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData('text/plain');
  var draggableElement = document.getElementById(data);
  var x = event.clientX;
  var y = event.clientY;

  var fontSize = Math.min(x, y) / 10;
  draggableElement.style.fontSize = fontSize + 'px';
}