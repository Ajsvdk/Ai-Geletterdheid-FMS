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

    // Add sort indicators and click handlers to table headers
    const headers = table.querySelectorAll('th');
    headers.forEach((header, index) => {
        header.style.cursor = 'pointer';
        header.dataset.sortDirection = 'none';
        header.addEventListener('click', () => sortTable(index));
        
        // Add sort indicator
        const span = document.createElement('span');
        span.className = 'sort-indicator';
        span.innerHTML = ' ↕️';
        header.appendChild(span);
    });

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
        const activeKosten = document.querySelector('.filter-section:nth-child(1) .filter-btn.active')?.dataset.filter;
        const selectedSpecialisme = specialismeSelect.value;

        rows.forEach((row, index) => {
            if (index === 0) return; // Skip header row

            const cells = row.getElementsByTagName('td');
            const text = row.textContent.toLowerCase();
            let showRow = text.includes(searchTerm);

            // Apply filters
            if (activeKosten === 'gratis') {
                showRow = showRow && (cells[2].textContent === '0' || cells[2].textContent.toLowerCase().includes('gratis'));
            } else if (activeKosten === 'betaald') {
                showRow = showRow && !(cells[2].textContent === '0' || cells[2].textContent.toLowerCase().includes('gratis'));
            }
            if (selectedSpecialisme !== 'all') {
                showRow = showRow && cells[6]?.textContent.toLowerCase().includes(selectedSpecialisme.toLowerCase());
            }

            row.style.display = showRow ? '' : 'none';
        });
    }

    function sortTable(columnIndex) {
        const tbody = table.querySelector('tbody') || table;
        const rows = Array.from(tbody.querySelectorAll('tr:not(:first-child)'));
        const header = headers[columnIndex];
        const currentDirection = header.dataset.sortDirection;
        
        // Reset all other headers
        headers.forEach(h => {
            if (h !== header) {
                h.dataset.sortDirection = 'none';
                h.querySelector('.sort-indicator').innerHTML = ' ↕️';
            }
        });

        // Update sort direction
        let direction = 'asc';
        if (currentDirection === 'none' || currentDirection === 'desc') {
            direction = 'asc';
            header.querySelector('.sort-indicator').innerHTML = ' ↑';
        } else {
            direction = 'desc';
            header.querySelector('.sort-indicator').innerHTML = ' ↓';
        }
        header.dataset.sortDirection = direction;

        // Sort rows
        const sortedRows = rows.sort((a, b) => {
            const aText = a.cells[columnIndex].textContent.trim();
            const bText = b.cells[columnIndex].textContent.trim();

            // Handle numeric values (like costs)
            const aNum = parseFloat(aText.replace(/[^0-9.-]+/g, ''));
            const bNum = parseFloat(bText.replace(/[^0-9.-]+/g, ''));

            if (!isNaN(aNum) && !isNaN(bNum)) {
                return direction === 'asc' ? aNum - bNum : bNum - aNum;
            }

            // Regular string comparison
            return direction === 'asc' 
                ? aText.localeCompare(bText, 'nl', {sensitivity: 'base'})
                : bText.localeCompare(aText, 'nl', {sensitivity: 'base'});
        });

        // Remove existing rows
        rows.forEach(row => row.remove());

        // Add sorted rows
        sortedRows.forEach(row => tbody.appendChild(row));
    }
}); 