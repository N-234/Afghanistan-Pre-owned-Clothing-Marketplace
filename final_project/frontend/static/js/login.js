const loginForm = document.querySelector("#login-form");
const loginMessage = document.querySelector("#login-message");

loginForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = new FormData(loginForm);

    const nextPage = new URLSearchParams(window.location.search).get("next");

    const loginUrl = nextPage
        ? "/login?next=" + encodeURIComponent(nextPage)
        : "/login";

    const response = await fetch(loginUrl, {
        method: "POST",
        body: formData
});

    const result = await response.json();

    loginMessage.textContent = result.message;
    if (result.success) {
    window.location.href = result.redirect;
}

});

loginForm.addEventListener("input", function () {
    loginMessage.textContent = "";
});