// Function to handle form submission for account creation
function handleCreateAccount(event) {
  event.preventDefault(); // Prevent the default form submission behavior

  // Get the values entered by the user
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;

  // Perform validation (you can add more complex validation as needed)
  if (username === "" || password === "") {
    alert("Please enter a username and password.");
    return;
  }

  // Send the data to the server for further processing (you need to implement this part)
  // Example: You can use AJAX or fetch() to send the data to a server-side script
  // and handle the account creation logic there.
}

// Function to handle form submission for login
function handleLogin(event) {
  event.preventDefault(); // Prevent the default form submission behavior

  // Get the values entered by the user
  var loginUsername = document.getElementById("loginUsername").value;
  var loginPassword = document.getElementById("loginPassword").value;

  // Perform validation (you can add more complex validation as needed)
  if (loginUsername === "" || loginPassword === "") {
    alert("Please enter your username and password.");
    return;
  }

  // Send the data to the server for further processing (you need to implement this part)
  // Example: You can use AJAX or fetch() to send the data to a server-side script
  // and handle the login logic there.
}

// Attach event listeners to the forms
var createAccountForm = document.getElementById("createAccountForm");
createAccountForm.addEventListener("submit", handleCreateAccount);

var loginForm = document.getElementById("loginForm");
loginForm.addEventListener("submit", handleLogin);
