const forgotForm = document.querySelector("#forgot-password-form");
const forgotMessage = document.querySelector("#forgot-password-message");
const sendButton = forgotForm.querySelector("button");

forgotForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    if (!forgotForm.reportValidity()) return;

    sendButton.disabled = true;
    forgotMessage.textContent = "Sending request...";

    try {
        const response = await fetch("/forgot-password", {
            method: "POST",
            body: new FormData(forgotForm)
        });

        const result = await response.json();

        if (response.ok && result.success) {
            forgotMessage.textContent =
                "If an account exists with this email, you will receive a password reset link.";
        } else {
            forgotMessage.textContent =
                "Could not process your request. Please try again later.";
        }
    } catch (error) {
        forgotMessage.textContent =
            "Could not connect. Please try again later.";
    } finally {
        sendButton.disabled = false;
    }
});