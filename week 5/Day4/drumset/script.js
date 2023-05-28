function playSound(event) {
    const keyCode = event.keyCode || this.getAttribute('data-key');
    const audio = document.querySelector(`audio[data-key="${keyCode}"]`);
    const key = document.querySelector(`.drum[data-key="${keyCode}"]`);
  
    if (!audio) return;}