function dragStart(event) {
    event.dataTransfer.setData("text/plain", event.target.id);
  }
  
  function allowDrop(event) {
    event.preventDefault();
  }
  
  function drop(event) {
    event.preventDefault();
    var data = event.dataTransfer.getData("text/plain");
    var draggableElement = document.getElementById(data);
    var dropzone = event.target;
  
    dropzone.appendChild(draggableElement);
  }
  
  var boxes = document.querySelectorAll('.box');
  boxes.forEach(function(box) {
    box.addEventListener('dragstart', dragStart);
  });
  
  var container = document.getElementById('container');
  container.addEventListener('dragover', allowDrop);
  container.addEventListener('drop', drop);