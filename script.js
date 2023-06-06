function toggleLoginForm() {
  var loginPopup = document.getElementById("login-popup");
  loginPopup.classList.toggle("show");
}

function toggleSignupForm() {
  var signupPopup = document.getElementById("signup-popup");
  signupPopup.classList.toggle("show");
}

function validateLoginForm() {
  // Add your login form validation logic here
  return true; // Return false if validation fails and prevent form submission
}

function validateSignupForm() {
  // Add your sign-up form validation logic here
  return true; // Return false if validation fails and prevent form submission
}
