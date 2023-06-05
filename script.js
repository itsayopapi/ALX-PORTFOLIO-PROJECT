// Toggle Login/Signup Form
function toggleLoginForm() {
  var loginPopup = document.getElementById("login-popup");
  loginPopup.style.display = (loginPopup.style.display === "block") ? "none" : "block";
}

// Form Validation
function validateLoginForm() {
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;

  if (email.trim() === "") {
    alert("Please enter your email.");
    return false;
  }

  if (password.trim() === "") {
    alert("Please enter your password.");
    return false;
  }

  return true;
}

function validateSignupForm() {
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;

  if (name.trim() === "") {
    alert("Please enter your name.");
    return false;
  }

  if (email.trim() === "") {
    alert("Please enter your email.");
    return false;
  }

  if (password.trim() === "") {
    alert("Please enter your password.");
    return false;
  }

  return true;
}

// Submit Form
document.getElementById("login-form").addEventListener("submit", function(event) {
  event.preventDefault();
  if (validateLoginForm()) {
    // Perform login logic here
    alert("Logged in successfully!");
  }
});

document.getElementById("signup-form").addEventListener("submit", function(event) {
  event.preventDefault();
  if (validateSignupForm()) {
    // Perform signup logic here
    alert("Signed up successfully!");
  }
});
