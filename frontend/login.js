const loginForm = document.querySelector("#login-form");
const loginMessage = document.querySelector("#login-message");

loginForm.addEventListener("submit", function (event) {
    event.preventDefault();

    loginMessage.textContent =
        "Form validation passed. Login needs the backend.";
});

loginForm.addEventListener("input", function () {
    loginMessage.textContent = "";
});