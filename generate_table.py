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
    
    # Generate markdown table with logo column
    table_lines = [
        "| Logo | Aanbieder | Titel | Doelgroep | Tijdsduur | Kosten | Link |",
        "|------|-----------|-------|-----------|-----------|--------|------|"
    ]
    
    for row in rows[1:]:  # Skip header
        if len(row) >= 2 and row[0].strip() and row[1].strip():
            # Escape pipe characters in all fields
            aanbieder = row[0].replace('|', '\\|') if len(row) > 0 else ""
            titel = row[1].replace('|', '\\|') if len(row) > 1 else ""
            doelgroep = row[2].replace('|', '\\|') if len(row) > 2 else ""
            tijdsduur = row[3].replace('|', '\\|') if len(row) > 3 else ""
            kosten = row[4].replace('|', '\\|') if len(row) > 4 else ""
            link = row[5].strip() if len(row) > 5 else ""
            
            # Generate favicon for logo column
            favicon_url = get_favicon_url(link)
            logo_cell = ""
            if favicon_url:
                logo_cell = f'<img src="{favicon_url}" alt="{aanbieder}" width="16" height="16" style="vertical-align: middle;">'
            
            # Handle link column
            link_cell = ""
            if link and link.startswith('http'):
                link_cell = f"[LINK]({link})"
            
            table_lines.append(f"| {logo_cell} | {aanbieder} | {titel} | {doelgroep} | {tijdsduur} | {kosten} | {link_cell} |")
    
    # Generate complete markdown content
    content = f"""# AI Scholingsaanbod

Overzicht van beschikbare AI-opleidingen voor zorgprofessionals.

## Cursussen en Trainingen

{chr(10).join(table_lines)}

## Bijdragen

Heeft u een AI-opleiding die nog niet in dit overzicht staat? [Voeg hem toe](bijdragen.html)!
"""
    
    # Write to markdown file
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Generated table with {len(table_lines)-2} entries")

if __name__ == "__main__":
    generate_table_from_csv() 