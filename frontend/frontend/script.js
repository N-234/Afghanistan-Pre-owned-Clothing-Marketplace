const searchInput = document.querySelector("#search");
const sizeFilter = document.querySelector("#size-filter");
const cards = document.querySelectorAll(".product-card");
const resultsCount = document.querySelector("#results-count");
const emptyMessage = document.querySelector("#empty-message");

function filterClothes() {
    const searchText = searchInput.value.trim().toLowerCase();
    const selectedSize = sizeFilter.value;
    let visibleCount = 0;

    cards.forEach(function (card) {
        const matchesSearch =
            card.textContent.toLowerCase().includes(searchText);

        const matchesSize =
            selectedSize === "all" ||
            card.dataset.size === selectedSize;

        const showCard = matchesSearch && matchesSize;
        card.hidden = !showCard;

        if (showCard) {
            visibleCount++;
        }
    });

    resultsCount.textContent = visibleCount + " clothes found";
    emptyMessage.hidden = visibleCount !== 0;
}

searchInput.addEventListener("input", filterClothes);
sizeFilter.addEventListener("change", filterClothes);

filterClothes();