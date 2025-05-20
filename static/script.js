document.addEventListener('DOMContentLoaded', function () {
    console.log("Script loaded");

    const manufacturingDateCheckbox = document.getElementById('manufacturingDate');
    const dateInput = document.getElementById('dateInput');
    const actionButton = document.getElementById('actionButton');
    const resultBox = document.getElementById('outputBox');

    dateInput.style.display = 'none';

    manufacturingDateCheckbox.addEventListener('change', function () {
        dateInput.style.display = this.checked ? 'block' : 'none';
        actionButton.textContent = this.checked ? 'Calculate Expiry Date' : 'Show Shelf Life';
    });

    const categoryDropdown = document.getElementById('categoryDropdown');
    const categoryDropdownContent = document.getElementById('categoryDropdownContent');
    const productSearchContainer = document.getElementById('productSearchContainer');

    categoryDropdown.addEventListener('click', function () {
        categoryDropdownContent.style.display = categoryDropdownContent.style.display === 'block' ? 'none' : 'block';
    });

    const categoryItems = document.querySelectorAll('.dropdown-item');
    categoryItems.forEach(item => {
        item.addEventListener('click', function () {
            const title = this.querySelector('.dropdown-item-title').textContent;
            categoryDropdown.querySelector('span').textContent = title;
            categoryDropdownContent.style.display = 'none';
        });
    });

    const storageOptions = document.querySelectorAll('.storage-option');
    storageOptions.forEach(option => {
        option.addEventListener('click', function () {
            storageOptions.forEach(opt => opt.classList.remove('active'));
            this.classList.add('active');
        });
    });

    const expiryTermsHeader = document.getElementById('expiryTermsHeader');
    const expiryContent = document.getElementById('expiryContent');
    const expiryArrow = document.getElementById('expiryArrow');
    expiryTermsHeader.addEventListener('click', function () {
        expiryContent.classList.toggle('active');
        expiryArrow.classList.toggle('arrow-down');
        expiryContent.style.display = expiryContent.classList.contains('active') ? 'block' : 'none';
    });

    const storageImpactHeader = document.getElementById('storageImpactHeader');
    const storageContent = document.getElementById('storageContent');
    const storageArrow = document.getElementById('storageArrow');
    storageImpactHeader.addEventListener('click', function () {
        storageContent.classList.toggle('active');
        storageArrow.classList.toggle('arrow-down');
        storageContent.style.display = storageContent.classList.contains('active') ? 'block' : 'none';
    });

    const warningHeader = document.getElementById('warningHeader');
    const warningContent = document.getElementById('warningContent');
    const warningArrow = document.getElementById('warningArrow');
    warningHeader.addEventListener('click', function () {
        warningContent.classList.toggle('active');
        warningArrow.classList.toggle('arrow-down');
        warningContent.style.display = warningContent.classList.contains('active') ? 'block' : 'none';
    });
    const tipsHeader = document.getElementById('tipsHeader');
const tipsContent = document.getElementById('tipsContent');
const tipsArrow = document.getElementById('tipsArrow');

tipsHeader.addEventListener('click', function () {
    tipsContent.classList.toggle('active');
    tipsArrow.classList.toggle('arrow-down');
    tipsContent.style.display = tipsContent.classList.contains('active') ? 'block' : 'none';
});


    const categorySearch = document.getElementById('categorySearch');
    const productSearch = document.getElementById('productSearch');

    categorySearch.addEventListener('click', function () {
        categorySearch.classList.add('active');
        productSearch.classList.remove('active');
        categoryDropdown.style.display = 'flex';
        productSearchContainer.style.display = 'none';
        categoryDropdownContent.style.display = 'block';
    });

    productSearch.addEventListener('click', function () {
        productSearch.classList.add('active');
        categorySearch.classList.remove('active');
        categoryDropdown.style.display = 'none';
        productSearchContainer.style.display = 'block';
        productSearchContainer.querySelector('input').focus();
    });

    document.addEventListener('click', function (event) {
        if (!categoryDropdown.contains(event.target) && !categorySearch.contains(event.target)) {
            categoryDropdownContent.style.display = 'none';
        }
    });

    // ✅ Handle action button click
    actionButton.addEventListener('click', async () => {
        const isProductSearch = productSearch.classList.contains('active');
        const manufacturingDate = manufacturingDateCheckbox.checked;
        const date = dateInput.value;
        const storage = document.querySelector('.storage-option.active')?.dataset?.storage;
        const opened = document.getElementById('openedToggle').checked;

        if (!storage) {
            resultBox.className = 'tagline error';
            resultBox.innerText = "Please select a storage condition.";
            return;
        }

        resultBox.className = 'tagline';
        resultBox.innerText = "Loading...";

        if (isProductSearch) {
            const product = document.querySelector('.product-search').value.trim();
            if (!product) {
                resultBox.className = 'tagline error';
                resultBox.innerText = "Please enter a product name.";
                return;
            }

            if (manufacturingDate && (!date || date === "Invalid Date")) {
                resultBox.className = 'tagline error';
                resultBox.innerText = "Please enter a valid manufacturing date.";
                return;
            }

            const payload = {
                product,
                storage,
                opened
            };
            if (manufacturingDate) payload.manufacturing_date = date;

            try {
                const res = await fetch('/get-product', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                const data = await res.json();

                if (data.status === 'success') {
                    if (data.expiry_date) {
                        const expiryDate = new Date(data.expiry_date);
                        const today = new Date();
                        const diffTime = today - expiryDate;
                        const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
                        let statusText = '';
                        let statusClass = '';

                        if (diffDays > 0) {
                            statusText = `❌ Expired ${diffDays} day(s) ago`;
                            statusClass = 'error';
                        } else {
                            statusText = `✅ Safe to use — ${Math.abs(diffDays)} day(s) left`;
                            statusClass = 'success';
                        }

                        resultBox.className = `tagline ${statusClass}`;
                        resultBox.innerHTML = `
                            <strong>Estimated Expiry Date:</strong> ${data.expiry_date}<br>
                            <strong>Status:</strong> ${statusText}
                        `;
                    } else {
                        resultBox.className = 'tagline success';
                        resultBox.innerText = `Estimated Shelf Life: ${data.shelf_life} days`;
                    }
                } else {
                    resultBox.className = 'tagline error';
                    resultBox.innerText = `❌ ${data.message}`;
                }
            } catch (err) {
                resultBox.className = 'tagline error';
                resultBox.innerText = "Something went wrong!";
                console.error(err);
            }

        } else {
            const selectedCategory = categoryDropdown.querySelector('span').innerText.toLowerCase().includes("medicine")
                ? "medicine"
                : "food";

            try {
                const res = await fetch('/get-category-average', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ category: selectedCategory })
                });

                const data = await res.json();

                resultBox.className = data.status === 'success' ? 'tagline success' : 'tagline error';
                resultBox.innerText = data.status === 'success'
                    ? `Approximate Shelf Life for ${selectedCategory} items (avg): ${data.average_shelf_life} days`
                    : `❌ ${data.message}`;
            } catch (err) {
                resultBox.className = 'tagline error';
                resultBox.innerText = "Something went wrong!";
                console.error(err);
            }
        }
    });
});
