const statusText = document.querySelector("#listing-status");
const soldButton = document.querySelector("#mark-sold-button");
const unavailableButton = document.querySelector("#mark-unavailable-button");
const availableButton = document.querySelector("#mark-available-button");
const deleteButton = document.querySelector("#delete-listing-button");
const soldMessage = document.querySelector("#sold-message");

const editForm = document.querySelector("#edit-listing-form");
const editMessage = document.querySelector("#edit-message");
const saveButton = editForm.querySelector("button");

const params = new URLSearchParams(window.location.search);
const listingId = params.get("id");


// Update listing status on the page
function updateListingStatus(status) {
    statusText.textContent =
        status === "available" ? "Available" :
        status === "sold" ? "Sold" :
        status === "unavailable" ? "Unavailable" :
        status === "removed" ? "Removed" :
        "Not loaded";

    soldButton.disabled = status !== "available";
    unavailableButton.disabled = status !== "available";
    availableButton.disabled = status !== "unavailable";
    deleteButton.disabled = status === "removed";

    soldButton.textContent =
        status === "sold" ? "Already Sold" : "Mark as Sold";

    unavailableButton.textContent =
        status === "unavailable" ? "Already Unavailable" : "Mark as Unavailable";

    availableButton.textContent =
        status === "available" ? "Already Available" : "Mark as Available";

    deleteButton.textContent =
        status === "removed" ? "Listing Removed" : "Delete Listing";
}


// Load listing information
async function loadListing() {
    saveButton.disabled = true;

    if (!listingId || !/^[1-9]\d*$/.test(listingId)) {
        editMessage.textContent =
            "Please open a listing from My Listings to edit it.";
        return;
    }

    editMessage.textContent = "Loading listing...";

    try {
        const response = await fetch(`/api/listings/${listingId}`);
        const result = await response.json();

        if (!response.ok || !result.success || !result.listing) {
            throw new Error("Could not load listing.");
        }

        const listing = result.listing;
        updateListingStatus(listing.status);

        editForm.elements.listing_id.value = listingId;

        const fields = [
            "title", "category", "price", "size",
            "condition", "city", "description"
        ];

        fields.forEach(function (field) {
            editForm.elements[field].value = listing[field] ?? "";
        });

        editMessage.textContent = "";
        saveButton.disabled = false;

    } catch (error) {
        editMessage.textContent =
            "Could not load this listing. Please try again later.";
    }
}


// Save listing changes
editForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    if (saveButton.disabled || !editForm.reportValidity()) return;

    const soldWasDisabled = soldButton.disabled;
    const unavailableWasDisabled = unavailableButton.disabled;
    const availableWasDisabled = availableButton.disabled;
    const deleteWasDisabled = deleteButton.disabled;

    saveButton.disabled = true;
    soldButton.disabled = true;
    unavailableButton.disabled = true;
    availableButton.disabled = true;
    deleteButton.disabled = true;

    editMessage.textContent = "Saving changes...";

    try {
        const response = await fetch(`/api/listings/${listingId}`, {
            method: "POST",
            body: new FormData(editForm)
        });

        const result = await response.json();

        if (response.ok && result.success) {
            editMessage.textContent = "Changes saved successfully.";
        } else {
            editMessage.textContent =
                "Could not save your changes. Please try again.";
        }

    } catch (error) {
        editMessage.textContent =
            "Could not connect. Please try again later.";

    } finally {
        saveButton.disabled = false;
        soldButton.disabled = soldWasDisabled;
        unavailableButton.disabled = unavailableWasDisabled;
        availableButton.disabled = availableWasDisabled;
        deleteButton.disabled = deleteWasDisabled;
    }
});


// Mark as Sold
soldButton.addEventListener("click", async function () {
    if (soldButton.disabled || !listingId) return;

    const confirmed = window.confirm("Mark this item as sold?");

    if (!confirmed) return;

    soldButton.disabled = true;
    unavailableButton.disabled = true;
    availableButton.disabled = true;
    deleteButton.disabled = true;
    saveButton.disabled = true;

    soldMessage.textContent = "Updating status...";

    try {
        const response = await fetch(
            `/api/listings/${listingId}/sold`,
            { method: "POST" }
        );

        const result = await response.json();

        if (!response.ok || !result.success) {
            throw new Error("Could not update status.");
        }

        updateListingStatus("sold");
        soldMessage.textContent = "Item marked as sold.";

    } catch (error) {
        soldMessage.textContent =
            "Could not update the status. Please try again.";

    } finally {
        saveButton.disabled = false;
    }
});


// Mark as Unavailable
unavailableButton.addEventListener("click", async function () {
    if (unavailableButton.disabled || !listingId) return;

    const confirmed = window.confirm(
        "Are you sure you want to mark this listing as unavailable?"
    );

    if (!confirmed) return;

    soldButton.disabled = true;
    unavailableButton.disabled = true;
    availableButton.disabled = true;
    deleteButton.disabled = true;
    saveButton.disabled = true;

    soldMessage.textContent = "Updating status...";

    try {
        const response = await fetch(
            `/api/listings/${listingId}/unavailable`,
            { method: "POST" }
        );

        const result = await response.json();

        if (!response.ok || !result.success) {
            throw new Error("Could not update status.");
        }

        updateListingStatus("unavailable");
        soldMessage.textContent = "Listing marked as unavailable.";

    } catch (error) {
        soldMessage.textContent =
            "Could not update the status. Please try again.";

    } finally {
        saveButton.disabled = false;
    }
});


// Mark as Available
availableButton.addEventListener("click", async function () {
    if (availableButton.disabled || !listingId) return;

    const confirmed = window.confirm(
        "Do you want to make this listing available again?"
    );

    if (!confirmed) return;

    soldButton.disabled = true;
    unavailableButton.disabled = true;
    availableButton.disabled = true;
    deleteButton.disabled = true;
    saveButton.disabled = true;

    soldMessage.textContent = "Updating status...";

    try {
        const response = await fetch(
            `/api/listings/${listingId}/available`,
            { method: "POST" }
        );

        const result = await response.json();

        if (!response.ok || !result.success) {
            throw new Error("Could not update status.");
        }

        updateListingStatus("available");
        soldMessage.textContent = "Listing is available again.";

    } catch (error) {
        soldMessage.textContent =
            "Could not update the status. Please try again.";

    } finally {
        saveButton.disabled = false;
    }
});


// Delete Listing (changes status to removed)
deleteButton.addEventListener("click", async function () {
    if (deleteButton.disabled || !listingId) return;

    const confirmed = window.confirm(
        "Are you sure you want to remove this listing? It will no longer appear in the marketplace."
    );

    if (!confirmed) return;

    deleteButton.disabled = true;
    soldButton.disabled = true;
    unavailableButton.disabled = true;
    availableButton.disabled = true;
    saveButton.disabled = true;

    soldMessage.textContent = "Removing listing...";

    try {
        const response = await fetch(
            `/api/listings/${listingId}/delete`,
            { method: "POST" }
        );

        const result = await response.json();

        if (!response.ok || !result.success) {
            throw new Error("Could not remove listing.");
        }

        updateListingStatus("removed");
        soldMessage.textContent = "Listing removed successfully.";

    } catch (error) {
        soldMessage.textContent =
            "Could not remove the listing. Please try again.";

    } finally {
        saveButton.disabled = false;
    }
});


// Start loading the listing
loadListing();