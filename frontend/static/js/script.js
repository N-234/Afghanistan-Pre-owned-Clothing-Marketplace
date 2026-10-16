const searchInput = document.querySelector("#search");
const sizeFilter = document.querySelector("#size-filter");
const priceFilter = document.querySelector("#price-filter");
const categoryFilter = document.querySelector("#category-filter");
const cards = document.querySelectorAll(".product-card");
const resultsCount = document.querySelector("#results-count");
const emptyMessage = document.querySelector("#empty-message");

function filterClothes() {
    const searchText = searchInput.value.trim().toLowerCase();
    const selectedSize = sizeFilter.value;
    const selectedPrice = priceFilter.value;
    const selectedCategory = categoryFilter.value;
    let visibleCount = 0;

    cards.forEach(function (card) {
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

searchInput.addEventListener("input", filterClothes);
sizeFilter.addEventListener("change", filterClothes);
priceFilter.addEventListener("change", filterClothes);
categoryFilter.addEventListener("change", filterClothes);

filterClothes();
document.querySelector("#clear-filters").addEventListener("click", function () {
    searchInput.value = "";
    sizeFilter.value = "all";
    priceFilter.value = "all";
    categoryFilter.value = "all";

    filterClothes();
});