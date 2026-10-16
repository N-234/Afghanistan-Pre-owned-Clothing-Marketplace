const loginForm = document.querySelector("#login-form");
const loginMessage = document.querySelector("#login-message");

loginForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = new FormData(loginForm);

    const response = await fetch("/login", {
        method: "POST",
        body: formData
    });

    const result = await response.json();

    loginMessage.textContent = result.message;
    if (result.success){
    window.location.href ="/";
}

});

loginForm.addEventListener("input", function () {
    loginMessage.textContent = "";
});