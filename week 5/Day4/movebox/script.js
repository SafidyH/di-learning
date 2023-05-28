function myMove() {
    var container = document.getElementById("container");
    var animate = document.getElementById("animate");
    var containerWidth = container.offsetWidth;
    var animateWidth = animate.offsetWidth;
    var position = 0;
    var speed = 1;
  
    var interval = setInterval(function() {
      if (position >= containerWidth - animateWidth) {
        clearInterval(interval);
      } else {
        position += speed;
        animate.style.left = position + "px";
      }
    }, 1);
  }