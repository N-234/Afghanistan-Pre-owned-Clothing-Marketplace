const messagesList = document.querySelector("#messages-list");
const inboxStatus = document.querySelector("#inbox-status");
const inboxEmpty = document.querySelector("#inbox-empty");
const inboxLogin = document.querySelector("#inbox-login");
const refreshButton = document.querySelector("#refresh-messages");

let loadingMessages = false;

function createMessageCard(message) {
    const card = document.createElement("article");
    card.className = "message-card";

    const title = document.createElement("h2");
    title.textContent = message.listing_title || "Clothing listing";

    const sender = document.createElement("p");
    sender.textContent = `From: ${message.sender_name || "Buyer"}`;

    const body = document.createElement("p");
    body.className = "message-body";
    body.textContent = message.message || "";

    const date = document.createElement("p");
    date.className = "message-date";

    const sentAt = new Date(message.created_at);

    date.textContent =
        message.created_at && !Number.isNaN(sentAt.getTime())
            ? sentAt.toLocaleString()
            : "Date unavailable";

    card.append(title, sender, body, date);
    return card;
}

async function loadMessages() {
    if (loadingMessages) return;

    loadingMessages = true;
    refreshButton.disabled = true;
    messagesList.setAttribute("aria-busy", "true");

    messagesList.replaceChildren();
    inboxEmpty.hidden = true;
    inboxLogin.hidden = true;
    inboxStatus.textContent = "Loading messages...";

    try {
        const response = await fetch("/api/messages/inbox", {
            cache: "no-store"
        });

        if (response.status === 401) {
            inboxStatus.textContent =
                "Please log in to view your inbox.";
            inboxLogin.hidden = false;
            return;
        }

        const result = await response.json();

        if (
            !response.ok ||
            !result.success ||
            !Array.isArray(result.messages)
        ) {
            throw new Error("Could not load messages.");
        }

        const cards = document.createDocumentFragment();

        result.messages.forEach(function (message) {
            cards.append(createMessageCard(message));
        });

        messagesList.replaceChildren(cards);
        inboxEmpty.hidden = result.messages.length !== 0;

        inboxStatus.textContent = result.messages.length
            ? `${result.messages.length} message(s) loaded.`
            : "";
    } catch (error) {
        inboxStatus.textContent =
            "Could not load messages. Please try Refresh Messages.";
    } finally {
        loadingMessages = false;
        refreshButton.disabled = false;
        messagesList.setAttribute("aria-busy", "false");
    }
}

refreshButton.addEventListener("click", loadMessages);

loadMessages();