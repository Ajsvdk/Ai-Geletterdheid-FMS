#!/usr/bin/env python3
"""
Script to generate the scholingsaanbod table from CSV data
"""
import csv
import os
from urllib.parse import urlparse

def get_favicon_url(website_url, size=16):
    """Generate favicon URL using Google's favicon API"""
    if not website_url or not website_url.startswith('http'):
        return ""
    
    try:
        # Extract domain from URL
        parsed_url = urlparse(website_url)
        domain = parsed_url.netloc
        
        # Remove 'www.' prefix if present
        if domain.startswith('www.'):
            domain = domain[4:]
            
        # Generate Google favicon API URL
        favicon_url = f"https://www.google.com/s2/favicons?domain={domain}&sz={size}"
        return favicon_url
    except:
        return ""

def truncate_text(text, max_length):
    """Truncate text if it's longer than max_length and add ellipsis"""
    if not text:
        return ""
    text = text.strip()
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."

def categorize_cost(cost_str):
    """Categorize cost as 'gratis' or 'betaald'"""
    if not cost_str or cost_str.strip() == "":
        return "onbekend"
    
    cost_lower = cost_str.lower()
    if "€0" in cost_str or "gratis" in cost_lower or cost_str.strip() == "0":
        return "gratis"
    else:
        return "betaald"

def generate_filter_javascript():
    """Generate JavaScript for table filtering"""
    return '''
<script>
function filterTable() {
    console.log('Filter function called'); // Debug log
    
    const doelgroepFilter = document.getElementById('doelgroep-filter').value;
    const tijdsduurFilter = document.getElementById('tijdsduur-filter').value;
    const kostenFilter = document.getElementById('kosten-filter').value;
    
    console.log('Filters:', doelgroepFilter, tijdsduurFilter, kostenFilter); // Debug log
    
    const table = document.getElementById('course-table');
    const tbody = table.getElementsByTagName('tbody')[0];
    const rows = tbody.getElementsByTagName('tr');
    
    console.log('Found', rows.length, 'rows'); // Debug log
    
    // Filter each row
    for (let i = 0; i < rows.length; i++) {
        const row = rows[i];
        const cells = row.getElementsByTagName('td');
        
        if (cells.length >= 7) {
            // Get cell content (0=Logo, 1=Aanbieder, 2=Titel, 3=Doelgroep, 4=Tijdsduur, 5=Kosten, 6=Link)
            const doelgroep = cells[3].textContent.trim();
            const tijdsduur = cells[4].textContent.trim();
            const kosten = cells[5].textContent.trim();
            
            // Categorize cost
            let kostenCategory = 'onbekend';
            if (kosten.includes('€0') || kosten.toLowerCase().includes('gratis') || kosten === '0') {
                kostenCategory = 'gratis';
            } else if (kosten.trim() !== '' && kosten.trim() !== 'n.v.t.' && kosten.trim() !== 'onbekend') {
                kostenCategory = 'betaald';
            }
            
            let showRow = true;
            
            // Apply doelgroep filter
            if (doelgroepFilter !== 'alle' && doelgroep !== doelgroepFilter) {
                showRow = false;
            }
            
            // Apply tijdsduur filter
            if (tijdsduurFilter !== 'alle') {
                const tijdsduurLower = tijdsduur.toLowerCase();
                if (tijdsduurFilter === 'kort') {
                    if (!tijdsduurLower.includes('uur') && !tijdsduurLower.includes('minuten')) {
                        showRow = false;
                    }
                } else if (tijdsduurFilter === 'middel') {
                    if (!tijdsduurLower.includes('dag')) {
                        showRow = false;
                    }
                } else if (tijdsduurFilter === 'lang') {
                    if (!tijdsduurLower.includes('week') && !tijdsduurLower.includes('maand')) {
                        showRow = false;
                    }
                }
            }
            
            // Apply kosten filter
            if (kostenFilter !== 'alle' && kostenCategory !== kostenFilter) {
                showRow = false;
            }
            
            // Show or hide row
            row.style.display = showRow ? '' : 'none';
        }
    }
}

// Add event listeners when page loads
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, adding event listeners'); // Debug log
    
    const doelgroepFilter = document.getElementById('doelgroep-filter');
    const tijdsduurFilter = document.getElementById('tijdsduur-filter');
    const kostenFilter = document.getElementById('kosten-filter');
    
    if (doelgroepFilter) {
        doelgroepFilter.addEventListener('change', filterTable);
        console.log('Doelgroep filter listener added');
    }
    if (tijdsduurFilter) {
        tijdsduurFilter.addEventListener('change', filterTable);
        console.log('Tijdsduur filter listener added');
    }
    if (kostenFilter) {
        kostenFilter.addEventListener('change', filterTable);
        console.log('Kosten filter listener added');
    }
});
</script>
'''

def generate_table_from_csv():
    csv_file = 'docs/ai_courses_cleaned.csv'
    md_file = 'docs/scholingsaanbod.md'
    
    if not os.path.exists(csv_file):
        print(f"CSV file {csv_file} not found")
        return
    
    # Read CSV data
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    if len(rows) < 2:
        print("Not enough data in CSV")
        return
    
    # Collect unique values for filters
    doelgroepen = set()
    for row in rows[1:]:
        if len(row) > 2:
            doelgroepen.add(row[2])
    
    # Generate filter controls
    filter_html = f'''
<div style="margin-bottom: 20px; padding: 15px; background-color: #f5f5f5; border-radius: 5px;">
    <div style="display: flex; gap: 20px; flex-wrap: wrap;">
        <div>
            <label for="doelgroep-filter" style="font-weight: bold;">Doelgroep:</label>
            <select id="doelgroep-filter" style="margin-left: 5px; padding: 5px;">
                <option value="alle">Alle</option>
                {chr(10).join([f'<option value="{doelgroep}">{doelgroep}</option>' for doelgroep in sorted(doelgroepen) if doelgroep.strip()])}
            </select>
        </div>
        <div>
            <label for="tijdsduur-filter" style="font-weight: bold;">Tijdsduur:</label>
            <select id="tijdsduur-filter" style="margin-left: 5px; padding: 5px;">
                <option value="alle">Alle</option>
                <option value="kort">Kort (uren/minuten)</option>
                <option value="middel">Middel (dagen)</option>
                <option value="lang">Lang (weken/maanden)</option>
            </select>
        </div>
        <div>
            <label for="kosten-filter" style="font-weight: bold;">Kosten:</label>
            <select id="kosten-filter" style="margin-left: 5px; padding: 5px;">
                <option value="alle">Alle</option>
                <option value="gratis">Gratis</option>
                <option value="betaald">Betaald</option>
            </select>
        </div>
    </div>
</div>
'''
    
    # Generate markdown table with logo column and ID for JavaScript
    table_lines = [
        '<table id="course-table" style="width: 100%; border-collapse: collapse;">',
        '<thead>',
        '<tr style="background-color: #f0f0f0;">',
        '<th style="border: 1px solid #ddd; padding: 8px;">Logo</th>',
        '<th style="border: 1px solid #ddd; padding: 8px;">Aanbieder</th>',
        '<th style="border: 1px solid #ddd; padding: 8px;">Titel</th>',
        '<th style="border: 1px solid #ddd; padding: 8px;">Doelgroep</th>',
        '<th style="border: 1px solid #ddd; padding: 8px;">Tijdsduur</th>',
        '<th style="border: 1px solid #ddd; padding: 8px;">Kosten</th>',
        '<th style="border: 1px solid #ddd; padding: 8px;">Link</th>',
        '</tr>',
        '</thead>',
        '<tbody>'
    ]
    
    for row in rows[1:]:  # Skip header
        if len(row) >= 2 and row[0].strip() and row[1].strip():
            # Escape HTML characters in all fields
            aanbieder = row[0].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;') if len(row) > 0 else ""
            titel = row[1].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;') if len(row) > 1 else ""
            doelgroep = row[2].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;') if len(row) > 2 else ""
            tijdsduur = row[3].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;') if len(row) > 3 else ""
            kosten = row[4].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;') if len(row) > 4 else ""
            link = row[5].strip() if len(row) > 5 else ""
            
            # Generate favicon for logo column
            favicon_url = get_favicon_url(link)
            logo_cell = ""
            if favicon_url:
                logo_cell = f'<img src="{favicon_url}" alt="{aanbieder}" width="16" height="16" style="vertical-align: middle;">'
            
            # Handle link column
            link_cell = ""
            if link and link.startswith('http'):
                link_cell = f'<a href="{link}" target="_blank">LINK</a>'
            
            # Truncate long text for display but keep full text for tooltip
            aanbieder_display = truncate_text(aanbieder, 25)
            titel_display = truncate_text(titel, 40)
            
            # Add title attribute for tooltip if text was truncated
            aanbieder_cell = f'<span title="{aanbieder}">{aanbieder_display}</span>' if len(aanbieder) > 25 else aanbieder_display
            titel_cell = f'<span title="{titel}">{titel_display}</span>' if len(titel) > 40 else titel_display
            
            table_lines.append(f'''<tr style="border: 1px solid #ddd;">
    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">{logo_cell}</td>
    <td style="border: 1px solid #ddd; padding: 8px;">{aanbieder_cell}</td>
    <td style="border: 1px solid #ddd; padding: 8px;">{titel_cell}</td>
    <td style="border: 1px solid #ddd; padding: 8px;">{doelgroep}</td>
    <td style="border: 1px solid #ddd; padding: 8px;">{tijdsduur}</td>
    <td style="border: 1px solid #ddd; padding: 8px;">{kosten}</td>
    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">{link_cell}</td>
</tr>''')
    
    table_lines.extend(['</tbody>', '</table>'])
    
    # Generate complete markdown content
    content = f"""#  AI-geletterdheid in de zorg: een praktisch overzicht

{filter_html}

{chr(10).join(table_lines)}

{generate_filter_javascript()}

## Bijdragen

Heeft u een AI-opleiding die nog niet in dit overzicht staat? [Voeg hem toe](bijdragen.html)!
"""
    
    # Write to markdown file
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Generated table with {len(table_lines)-4} entries")

if __name__ == "__main__":
    generate_table_from_csv() 