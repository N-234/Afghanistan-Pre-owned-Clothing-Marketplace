const form = document.querySelector("#signup-form");
const password = document.querySelector("#password");
const confirmation = document.querySelector("#confirm-password");
const message = document.querySelector("#signup-message");

function checkPasswords() {
    const mismatch = confirmation.value !== password.value;

    confirmation.setCustomValidity(
        mismatch ? "Passwords do not match." : ""
    );
    message.textContent = "";
}

password.addEventListener("input", checkPasswords);
confirmation.addEventListener("input", checkPasswords);

form.addEventListener("submit", function (event) {
    event.preventDefault();

    checkPasswords();

    if (!form.reportValidity()) {
        return;
    }

    message.textContent =
        "Form validation passed. Account creation needs the backend.";
});
