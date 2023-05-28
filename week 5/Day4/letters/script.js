const lettersInput = document.getElementById('lettersInput');

lettersInput.addEventListener('input', function(event) {
  const inputValue = event.target.value;
  const sanitizedValue = inputValue.replace(/[^A-Za-z]/g, '');
  event.target.value = sanitizedValue;
});