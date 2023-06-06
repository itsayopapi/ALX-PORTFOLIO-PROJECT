function toggleLoginForm() {
  var loginPopup = document.getElementById("login-popup");
  loginPopup.style.display = loginPopup.style.display === "none" ? "block" : "none";
}

function toggleSignupForm() {
  var signupPopup = document.getElementById("signup-popup");
  signupPopup.style.display = signupPopup.style.display === "none" ? "block" : "none";
}

function validateLoginForm() {
  // Add your login form validation logic here
  return true;
}

function validateSignupForm() {
  // Add your signup form validation logic here
  return true;
}
