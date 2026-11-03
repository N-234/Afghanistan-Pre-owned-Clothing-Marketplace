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

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    checkPasswords();

    if (!form.reportValidity()) {
        return;
    }

 const formData = new FormData(form);

    const response = await fetch("/signup", {
        method: "POST",
        body: formData
    });

    const result = await response.json();

    message.textContent = result.message;

    if (result.success) {
        form.reset();
    }
});