<div align="center">
  <img src="docs/assets/logo.svg" alt="AI-geletterdheid in de zorg" width="120" height="120">
  
  # AI-geletterdheid in de zorg: een praktisch overzicht

  [![Website](https://img.shields.io/website?url=https%3A%2F%2Fajsvdk.github.io%2FAi-Geletterdheid-FMS%2F&up_message=live&up_color=brightgreen&down_message=offline&down_color=red&style=flat-square&label=status)](https://ajsvdk.github.io/Ai-Geletterdheid-FMS/)
  [![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=flat-square)](LICENSE)
  [![GitHub Pages](https://img.shields.io/badge/deployed%20on-GitHub%20Pages-blue?style=flat-square&logo=github)](https://ajsvdk.github.io/Ai-Geletterdheid-FMS/)

  De zorgsector bevindt zich in een stroomversnelling door de opkomst van kunstmatige intelligentie (AI). Deze open source website biedt een actueel overzicht van beschikbaar AI-onderwijs voor zorgprofessionals.

  🌐 **Live website**: [ajsvdk.github.io/Ai-Geletterdheid-FMS](https://ajsvdk.github.io/Ai-Geletterdheid-FMS/)
</div>

## Waarom dit platform?

Zorgprofessionals zoeken naar manieren waarop zij zich kunnen oriënteren op het onderwijsaanbod rondom AI, toegespitst op de zorgprofessional. Met de komst van de Europese AI-verordening is AI-geletterdheid niet alleen leuk of handig, maar ook een wettelijke verplichting.

Deze site helpt je bij het vinden van:
- Cursussen en e-modules over AI in de zorg
- Praktische informatie zoals tijdsinvestering, kosten en doelgroepen  
- Training op verschillende niveaus: van basis tot expert
- Specifieke scholing per specialisme


## Voor ontwikkelaars

### Lokaal draaien

```bash
# Clone de repository
git clone https://github.com/ajsvdk/Ai-Geletterdheid-FMS.git
cd Ai-Geletterdheid-FMS

# Installeer dependencies
pip install -r requirements.txt

# Start de development server
mkdocs serve
```

De site wordt automatisch beschikbaar op `http://127.0.0.1:8000/Ai-Geletterdheid-FMS/`

### Cursusdata bijwerken

```bash
# Bewerk de CSV file
vim docs/ai_courses_cleaned.csv

# Regenereer de filterable table met logo's
python generate_table.py
```

De `generate_table.py` script:
- Leest de CSV data
- Genereert automatisch favicons van provider websites  
- Maakt een interactieve HTML table met filters
- Houdt tekst beknopt met tooltips voor volledige info

### Deployment

De website wordt automatisch gedeployed naar GitHub Pages via GitHub Actions wanneer je naar de `main` branch pusht.

**Belangrijke bestanden:**
- `docs/ai_courses_cleaned.csv` - De cursusdata
- `generate_table.py` - Script voor table generatie
- `mkdocs.yml` - Site configuratie
- `.github/workflows/` - Automatische deployment

## Open en samen

Deze site is een open-source initiatief. Iedereen kan bijdragen:

### Voor zorgprofessionals
- **Cursussen toevoegen** via het formulier op de website
- **Suggesties delen** voor verbeteringen

### Voor ontwikkelaars  
- **Code bijdragen** via GitHub pull requests
- **Features voorstellen** via GitHub issues
- **Documentatie verbeteren**

## Belangrijke kanttekening

Deze site pretendeert geen volledig overzicht te geven van al het beschikbare onderwijs online en offline met betrekking tot informatiekunde, datawetenschap of AI. Daarvoor ontbreekt het ons aan middelen. Ingezonden suggesties worden opgenomen op relevantie en volledigheid, met als doel de kwaliteit van het overzicht te bewaken en spam te voorkomen.

## Contact en vragen

- 📧 **Email**: [aionderwijszorg@gmail.com](mailto:aionderwijszorg@gmail.com)  
- 💻 **GitHub**: [Ai-Geletterdheid-FMS](https://github.com/ajsvdk/Ai-Geletterdheid-FMS)
- 🌐 **Website**: [ajsvdk.github.io/Ai-Geletterdheid-FMS](https://ajsvdk.github.io/Ai-Geletterdheid-FMS/)

## Licentie

Dit project valt onder de [Apache 2.0 licentie](LICENSE). Je bent vrij om de code of inhoud te hergebruiken, aan te passen en te distribueren, mits met bronvermelding en onder dezelfde licentievoorwaarden.

---

**Auteur**: A.J.S. (Auke) van der Kuil  
**In opdracht van**: Commissie A.I. van de [Federatie Medisch Specialisten (FMS)](https://demedischspecialist.nl/themas/thema/artificial-intelligence-ai)

*Dit overzicht wordt regelmatig bijgewerkt en leeft door jullie bijdragen.*


