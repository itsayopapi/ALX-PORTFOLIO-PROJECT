function toggleSignupForm() {
  var signupForm = document.getElementById("signup-popup");
  signupForm.classList.toggle("show");
}

function toggleLoginForm() {
  var signupForm = document.getElementById("signup-popup");
  signupForm.classList.remove("show");

  var loginForm = document.getElementById("login-popup");
  loginForm.classList.toggle("show");
}

function validateSignupForm() {
  // Add your validation logic here
  return true; // For demonstration purposes, always return true
}

function validateLoginForm() {
  // Add your validation logic here
  return true; // For demonstration purposes, always return true
}

document.getElementById("get-started-btn").addEventListener("click", toggleSignupForm);
