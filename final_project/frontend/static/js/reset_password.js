const resetForm = document.querySelector("#reset-password-form");
const passwordInput = document.querySelector("#new-password");
const confirmInput = document.querySelector("#confirm-password");
const tokenInput = document.querySelector("#reset-token");
const resetMessage = document.querySelector("#reset-password-message");
const resetButton = resetForm.querySelector("button");

const params = new URLSearchParams(window.location.search);
tokenInput.value = params.get("token") || "";

confirmInput.addEventListener("input", function () {
    confirmInput.setCustomValidity("");
});

passwordInput.addEventListener("input", function () {
    confirmInput.setCustomValidity("");
});

resetForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    confirmInput.setCustomValidity(
        passwordInput.value === confirmInput.value
            ? ""
            : "Passwords do not match."
    );

    if (!resetForm.reportValidity()) return;

    if (!tokenInput.value) {
        resetMessage.textContent =
            "Reset link is missing. Please request a new link.";
        return;
    }

    resetButton.disabled = true;
    resetMessage.textContent = "Updating password...";

    try {
        const response = await fetch("/reset-password", {
            method: "POST",
            body: new FormData(resetForm)
        });

        const result = await response.json();

        if (response.ok && result.success) {
            resetForm.reset();
            resetMessage.textContent =
                "Password updated successfully. You can now log in.";
        } else {
            resetMessage.textContent =
                "Could not reset your password. Please request a new link.";
        }
    } catch (error) {
        resetMessage.textContent =
            "Could not connect. Please try again later.";
    } finally {
        resetButton.disabled = false;
    }
});