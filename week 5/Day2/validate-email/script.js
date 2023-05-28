const emailForm = document.getElementById('emailForm');
const emailInput = document.getElementById('email');

emailForm.addEventListener('submit', function(event) {
  event.preventDefault();
  const email = emailInput.value;
  const isValid = validateEmail(email);
  if (isValid) {
    alert('Email is valid!');
  } else {
    alert('Invalid email address!');
  }
});

function validateEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}