
const searchInput = document.querySelector("#search");
const sizeFilter = document.querySelector("#size-filter");
const priceFilter = document.querySelector("#price-filter");
const categoryFilter = document.querySelector("#category-filter");
const cards = document.querySelectorAll(".product-card");
const resultsCount = document.querySelector("#results-count");
const emptyMessage = document.querySelector("#empty-message");
const clearButton = document.querySelector("#clear-filters");
const sortFilter = document.querySelector("#sort-filter");
const productGrid = document.querySelector(".product-grid");

// Filter and sort clothes
function filterClothes() {
    const searchText = searchInput.value.trim().toLowerCase();
    const selectedSize = sizeFilter.value;
    const selectedPrice = priceFilter.value;
    const selectedCategory = categoryFilter.value;
    const selectedSort = sortFilter.value;

    let visibleCount = 0;

    // Convert cards to an array
    const cardArray = Array.from(cards);

    // Sort clothes
cardArray.sort(function (a, b) {
    const priceA = Number(
        a.querySelector(".price").textContent.replace(/[^0-9.]/g, "")
    );

    const priceB = Number(
        b.querySelector(".price").textContent.replace(/[^0-9.]/g, "")
    );

    if (selectedSort === "price-low") {
        return priceA - priceB;
    }

    if (selectedSort === "price-high") {
        return priceB - priceA;
    }

    if (selectedSort === "oldest") {
        return Number(a.dataset.id) - Number(b.dataset.id);
    }

    if (selectedSort === "newest") {
        return Number(b.dataset.id) - Number(a.dataset.id);
    }

    return 0;
});

// Put sorted cards back in the product grid
cardArray.forEach(function (card) {
    productGrid.appendChild(card);
});
    // Apply filters
    cardArray.forEach(function (card) {
        const matchesSearch =
            card.textContent.toLowerCase().includes(searchText);

        const matchesSize =
            selectedSize === "all" ||
            card.dataset.size === selectedSize;

        const priceText = card.querySelector(".price").textContent;
        const price = Number(priceText.replace(/[^0-9.]/g, ""));

        const matchesPrice =
            selectedPrice === "all" ||
            price <= Number(selectedPrice);

        const matchesCategory =
            selectedCategory === "all" ||
            card.dataset.category === selectedCategory;

        const showCard =
            matchesSearch && matchesSize && matchesPrice && matchesCategory;

        card.hidden = !showCard;

        if (showCard) {
            visibleCount++;
        }
    });

    resultsCount.textContent = visibleCount + " clothes found";
    emptyMessage.hidden = visibleCount !== 0;
}

// Run filters only on pages that have the filter elements
if (
     searchInput &&
    sizeFilter &&
    priceFilter &&
    categoryFilter &&
    sortFilter &&
    resultsCount &&
    emptyMessage &&
    clearButton
) {
    searchInput.addEventListener("input", filterClothes);
    sizeFilter.addEventListener("change", filterClothes);
    priceFilter.addEventListener("change", filterClothes);
    categoryFilter.addEventListener("change", filterClothes);
    sortFilter.addEventListener("change", filterClothes);

    clearButton.addEventListener("click", function () {
        searchInput.value = "";
        sizeFilter.value = "all";
        priceFilter.value = "all";
        categoryFilter.value = "all";
        sortFilter.value = "newest";

        filterClothes();
    });

    filterClothes();
}

// Load user notifications
function loadNotifications() {
    const notificationList = document.querySelector("#notificationList");
    const notificationCount = document.querySelector("#notificationCount");

    if (!notificationList || !notificationCount) {
        return;
    }

    fetch("/api/notifications")
        .then(response => response.json())
        .then(data => {
            if (!data.success) {
                return;
            }

            const notifications = data.notifications;

            // Show only unread notifications
            const unreadNotifications = notifications.filter(function(notification) {
                return notification.is_read === 0;
            });

            notificationCount.textContent = unreadNotifications.length;
            notificationCount.style.display =
                unreadNotifications.length > 0 ? "inline-block" : "none";

            notificationList.innerHTML = "";

            if (unreadNotifications.length === 0) {
                notificationList.textContent = "No new notifications.";
                return;
            }

            unreadNotifications.forEach(function(notification) {
                const item = document.createElement("div");
                item.className = "notification-item unread";

                item.style.cursor = "pointer";

                item.addEventListener("click", function() {
                    window.location.href = "/inbox";
                });

                const message = document.createElement("p");
                message.textContent = notification.message;
                item.appendChild(message);

                const date = document.createElement("small");
                date.textContent = notification.created_at;
                item.appendChild(date);

                notificationList.appendChild(item);
            });
        });
}

// Load notifications when the page opens
document.addEventListener("DOMContentLoaded", loadNotifications);