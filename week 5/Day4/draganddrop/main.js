var box = document.getElementById("box");
var target = document.getElementById("target");
var isDragging = false;

box.addEventListener("mousedown", function(event) {
  isDragging = true;
});

document.addEventListener("mousemove", function(event) {
  if (isDragging) {
    box.style.left = event.clientX - box.offsetWidth / 2 + "px";
    box.style.top = event.clientY - box.offsetHeight / 2 + "px";
  }
});

document.addEventListener("mouseup", function(event) {
  isDragging = false;
  if (isInsideTarget(event.clientX, event.clientY)) {
    box.style.backgroundColor = "green";
  } else {
    box.style.backgroundColor = "red";
  }
});

function isInsideTarget(x, y) {
  var targetRect = target.getBoundingClientRect();
  return (
    x >= targetRect.left &&
    x <= targetRect.right &&
    y >= targetRect.top &&
    y <= targetRect.bottom
  );
}