const sellForm = document.querySelector("#sell-form");
const photoInput = document.querySelector("#photo");
const photoPreview = document.querySelector("#photo-preview");
const sellMessage = document.querySelector("#sell-message");
const previewButton = sellForm.querySelector("button");

let previewUrl = "";

previewButton.disabled = false;

photoInput.addEventListener("change", function () {
    photoInput.setCustomValidity("");
    sellMessage.textContent = "";
    photoPreview.hidden = true;
    photoPreview.removeAttribute("src");

    if (previewUrl) {
        URL.revokeObjectURL(previewUrl);
        previewUrl = "";
    }

    const file = photoInput.files[0];

    if (!file) {
        return;
    }

    const allowedTypes = [
        "image/jpeg",
        "image/png",
        "image/webp"
    ];

    if (!allowedTypes.includes(file.type)) {
        photoInput.setCustomValidity("Choose a JPG, PNG or WebP image.");
        photoInput.reportValidity();
        return;
    }

    if (file.size > 5 * 1024 * 1024) {
        photoInput.setCustomValidity("Choose an image of 5 MB or smaller.");
        photoInput.reportValidity();
        return;
    }

    previewUrl = URL.createObjectURL(file);
    photoPreview.src = previewUrl;
    photoPreview.hidden = false;
});

sellForm.addEventListener("input", function () {
    sellMessage.textContent = "";
});


    sellForm.addEventListener("submit", function (event) {
        event.preventDefault();

        if (!sellForm.reportValidity() || !previewUrl) {
            return;
        }

        const fields = [
            ["#listing-title", "#item-name", ""],
            ["#listing-category", "#category", "Category: "],
            ["#listing-size", "#size", "Size: "],
            ["#listing-condition", "#condition", "Condition: "],
            ["#listing-city", "#city", "City: "],
            ["#listing-description", "#description", ""]
        ];

        fields.forEach(function ([target, source, label]) {
            const input = document.querySelector(source);

            const value = input.tagName === "SELECT"
                ? input.selectedOptions[0].textContent
                : input.value.trim();

            document.querySelector(target).textContent = label + value;
        });

        const price = document.querySelector("#price").valueAsNumber;

        document.querySelector("#listing-price").textContent =
            price.toLocaleString("en-US") + " AFN";

        document.querySelector("#listing-photo").src = previewUrl;

        const preview = document.querySelector("#listing-preview");
        preview.hidden = false;

        sellMessage.textContent =
            "Preview updated. Your listing has not been published.";

        preview.scrollIntoView({block: "start"});
    });

    sellForm.addEventListener("input", function () {
        document.querySelector("#listing-preview").hidden = true;
    });

    sellForm.addEventListener("change", function () {
        document.querySelector("#listing-preview").hidden = true;
    });
