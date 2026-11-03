const contactForm = document.querySelector("#contact-seller-form");
const messageInput = document.querySelector("#message");
const sendButton = document.querySelector("#send-message-button");
const contactMessage = document.querySelector("#contact-message");
const listingSummary = document.querySelector("#listing-summary");

const params = new URLSearchParams(window.location.search);
const listingId = params.get("id");

let listingLoaded = false;
let sending = false;

async function loadListing() {
    if (!listingId || !/^[1-9]\d*$/.test(listingId)) {
        listingSummary.textContent =
            "Please select a clothing item before contacting the seller.";
        return;
    }

    try {
        const response = await fetch(
            `/api/listings/${listingId}`
        );
        const result = await response.json();

        if (!response.ok || !result.success || !result.listing) {
            throw new Error("Could not load listing.");
        }

        listingSummary.textContent =
    `About: ${result.listing.title}`;

if (result.listing.user_id == window.currentUserId) {
    contactMessage.textContent =
        "This is your own listing. You cannot message yourself.";
    messageInput.disabled = true;
    sendButton.disabled = true;
    return;
}

listingLoaded = true;
sendButton.disabled = false;
    } catch (error) {
        listingSummary.textContent =
            "Could not load this item. Please try again later.";
    }
}

contactForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    if (!listingLoaded || sending) return;

    messageInput.setCustomValidity("");

    const message = messageInput.value.trim();

    if (!message) {
        messageInput.setCustomValidity("Please write a message.");
    }

    if (!contactForm.reportValidity()) return;

    sending = true;
    sendButton.disabled = true;
    messageInput.readOnly = true;
    contactMessage.textContent = "Sending message...";

    try {
        const response = await fetch(
            `/api/listings/${listingId}/messages`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ message })
            }
        );

        if (response.status === 401) {
            contactMessage.textContent =
                "Please log in before sending a message.";
            return;
        }

        const result = await response.json();

        if (!response.ok || !result.success) {
            throw new Error("Could not send message.");
        }

        messageInput.value = "";
        contactMessage.textContent = "Message sent successfully.";
    } catch (error) {
        contactMessage.textContent =
            "Could not send your message. Please try again.";
    } finally {
        sending = false;
        sendButton.disabled = false;
        messageInput.readOnly = false;
    }
});

messageInput.addEventListener("input", function () {
    messageInput.setCustomValidity("");
});

loadListing();