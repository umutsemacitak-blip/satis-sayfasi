document.addEventListener('DOMContentLoaded', () => {
    const mainCardContainer = document.getElementById('main-card-container');
    const subCardContainer = document.getElementById('sub-card-container');
    const backButton = document.getElementById('back-button');
    const pageTitle = document.getElementById('page-title');

    const categories = [
        { id: 1, title: 'Category 1' },
        { id: 2, title: 'Category 2' },
        { id: 3, title: 'Category 3' },
        { id: 4, title: 'Category 4' },
        { id: 5, title: 'Category 5' },
        { id: 6, title: 'Category 6' },
        { id: 7, title: 'Category 7' },
        { id: 8, title: 'Category 8' },
    ];

    // Function to create a single card
    function createCard(title, isSubCard = false) {
        const card = document.createElement('div');
        card.className = 'card';
        const cardTitle = document.createElement('h3');
        cardTitle.textContent = title;
        card.appendChild(cardTitle);
        if (!isSubCard) {
            card.onclick = () => showSubCards(title);
        }
        return card;
    }

    // Function to show the main category cards
    function showMainCards() {
        mainCardContainer.innerHTML = '';
        subCardContainer.innerHTML = '';

        categories.forEach(category => {
            const card = createCard(category.title);
            mainCardContainer.appendChild(card);
        });

        pageTitle.textContent = 'Main Categories';
        mainCardContainer.style.display = 'grid';
        subCardContainer.style.display = 'none';
        backButton.style.display = 'none';
    }

    // Function to show the sub-cards for a selected category
    function showSubCards(categoryTitle) {
        subCardContainer.innerHTML = '';
        for (let i = 1; i <= 20; i++) {
            const subCard = createCard(`${categoryTitle} - Item ${i}`, true);
            subCardContainer.appendChild(subCard);
        }

        pageTitle.textContent = categoryTitle;
        mainCardContainer.style.display = 'none';
        subCardContainer.style.display = 'grid';
        backButton.style.display = 'block';
    }

    // Event listener for the back button
    backButton.addEventListener('click', showMainCards);

    // Initial load
    showMainCards();
});