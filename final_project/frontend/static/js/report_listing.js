
const reportForm = document.getElementById("report-form");

reportForm.addEventListener("submit", async function(event) {
    event.preventDefault();

    const listingId = document.getElementById("report-listing-id").value;
    const reason = document.getElementById("report-reason").value;
    const details = document.getElementById("report-details").value;
    const message = document.getElementById("report-message");

    try {
        const response = await fetch("/api/listings/" + listingId + "/report", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                reason: reason,
                details: details
            })
        });

        const result = await response.json();

        console.log("Server response:", response.status, result);

        message.textContent = result.message || "Report submission failed.";

        if (result.success) {
            reportForm.reset();
        }

    } catch (error) {
        console.error("Report error:", error);
        message.textContent = "Something went wrong. Check the Flask terminal for details.";
    }
});
