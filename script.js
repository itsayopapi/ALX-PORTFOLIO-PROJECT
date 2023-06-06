function toggleLoginForm() {
  var loginPopup = document.getElementById('login-popup');
  loginPopup.classList.toggle('show-popup');
}

function toggleSignupForm() {
  var signupForm = document.getElementById('signup-form');
  signupForm.classList.toggle('show-form');
}

function validateLoginForm() {
  var emailInput = document.getElementById('login-email');
  var passwordInput = document.getElementById('login-password');

  if (emailInput.value === '') {
    alert('Please enter your email.');
    return false;
  }

  if (passwordInput.value === '') {
    alert('Please enter your password.');
    return false;
  }

  // Perform login logic here

  return true;
}
