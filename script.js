// Toggle login/signup pop-up forms
function toggleLoginForm() {
  var loginPopup = document.getElementById("login-popup");
  loginPopup.style.display = (loginPopup.style.display === "block") ? "none" : "block";
}

function toggleSignupForm() {
  var signupPopup = document.getElementById("signup-popup");
  signupPopup.style.display = (signupPopup.style.display === "block") ? "none" : "block";
}
