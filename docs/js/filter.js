document.addEventListener('DOMContentLoaded', function() {
    // Add filter inputs
    const tableContainer = document.querySelector('table').parentElement;
    const filterDiv = document.createElement('div');
    filterDiv.className = 'course-filters';
    filterDiv.innerHTML = `
        <div class="filter-group">
            <input type="text" id="searchInput" placeholder="🔍 Zoeken..." class="search-input">
            <div class="filter-categories">
                <div class="filter-section">
                    <h4>Doelgroep</h4>
                    <div class="filter-buttons">
                        <button class="filter-btn active" data-filter="all">Alle cursussen</button>
                        <button class="filter-btn" data-filter="artsen">Voor Artsen</button>
                    </div>
                </div>
                <div class="filter-section">
                    <h4>Kosten</h4>
                    <div class="filter-buttons">
                        <button class="filter-btn" data-filter="gratis">Gratis</button>
                        <button class="filter-btn" data-filter="betaald">Betaald</button>
                    </div>
                </div>
                <div class="filter-section">
                    <h4>Specialisme</h4>
                    <select id="specialismeFilter" class="filter-select">
                        <option value="all">Alle specialismen</option>
                        <option value="radiologie">Radiologie</option>
                        <option value="pathologie">Pathologie</option>
                        <option value="interne">Interne Geneeskunde</option>
                        <option value="chirurgie">Chirurgie</option>
                        <option value="huisarts">Huisartsgeneeskunde</option>
                    </select>
                </div>
            </div>
            <div class="active-filters" id="activeFilters"></div>
        </div>
    `;
    
    tableContainer.insertBefore(filterDiv, tableContainer.firstChild);

    // Add event listeners
    const searchInput = document.getElementById('searchInput');
    const filterButtons = document.querySelectorAll('.filter-btn');
    const specialismeSelect = document.getElementById('specialismeFilter');
    const table = document.querySelector('table');
    const rows = table.querySelectorAll('tr');
    const activeFilters = document.getElementById('activeFilters');

    // Search functionality
    searchInput.addEventListener('input', filterTable);
    filterButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            const section = e.target.closest('.filter-section');
            section.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
            e.target.classList.add('active');
            updateActiveFilters();
            filterTable();
        });
    });

    specialismeSelect.addEventListener('change', () => {
        updateActiveFilters();
        filterTable();
    });

    function updateActiveFilters() {
        const filters = [];
        document.querySelectorAll('.filter-btn.active').forEach(btn => {
            if (btn.dataset.filter !== 'all') {
                filters.push(`<span class="filter-tag">${btn.textContent} <button onclick="removeFilter(this)" data-filter="${btn.dataset.filter}">×</button></span>`);
            }
        });
        if (specialismeSelect.value !== 'all') {
            filters.push(`<span class="filter-tag">${specialismeSelect.options[specialismeSelect.selectedIndex].text} <button onclick="removeFilter(this)" data-filter="specialisme">×</button></span>`);
        }
        activeFilters.innerHTML = filters.join('');
    }

    window.removeFilter = function(button) {
        const filter = button.dataset.filter;
        if (filter === 'specialisme') {
            specialismeSelect.value = 'all';
        } else {
            document.querySelector(`.filter-btn[data-filter="${filter}"]`).closest('.filter-section')
                .querySelector('[data-filter="all"]').click();
        }
        filterTable();
    };

    function filterTable() {
        const searchTerm = searchInput.value.toLowerCase();
        const activeDoelgroep = document.querySelector('.filter-section:first-child .filter-btn.active').dataset.filter;
        const activeKosten = document.querySelector('.filter-section:nth-child(2) .filter-btn.active')?.dataset.filter;
        const selectedSpecialisme = specialismeSelect.value;

        rows.forEach((row, index) => {
            if (index === 0) return; // Skip header row

            const cells = row.getElementsByTagName('td');
            const text = row.textContent.toLowerCase();
            let showRow = text.includes(searchTerm);

            // Apply filters
            if (activeDoelgroep === 'artsen') {
                showRow = showRow && cells[2].textContent.toLowerCase().includes('ja');
            }
            if (activeKosten === 'gratis') {
                showRow = showRow && (cells[3].textContent === '0' || cells[3].textContent.toLowerCase().includes('gratis'));
            } else if (activeKosten === 'betaald') {
                showRow = showRow && !(cells[3].textContent === '0' || cells[3].textContent.toLowerCase().includes('gratis'));
            }
            if (selectedSpecialisme !== 'all') {
                showRow = showRow && cells[8]?.textContent.toLowerCase().includes(selectedSpecialisme.toLowerCase());
            }

            row.style.display = showRow ? '' : 'none';
        });
    }
}); 