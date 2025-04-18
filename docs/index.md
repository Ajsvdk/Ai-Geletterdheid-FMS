# Scholingsaanbod AI

Voorlopige uitwerking van het scholingsaanbod AI. Hieronder vind je enkele aanbevolen cursussen en de doelstellingen van deze site:

**Doel van deze site:**
- Makkelijk bij te werken
- Beste aanbieders identificeren
- Overzichtelijk presenteren
- Open-source

![Voorbeeld schermindeling](https://github.com/user-attachments/assets/46d7a7a3-ae7e-4c52-a753-7f1fa6f134d6)

## Aanbevolen cursussen

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 px-4">
{% for c in courses %}
  <div class="card p-4 shadow-lg rounded-lg">
    <h3 class="text-xl font-bold">{{ c['Titel'] }}</h3>
    <p class="text-gray-600">{{ c['Aanbieder'] }}</p>
    <p class="mt-2 font-semibold">{{ c['Kosten'] }}</p>
    <a href="{{ c['Link'] }}" class="mt-4 inline-block px-4 py-2 bg-blue-500 text-white rounded">
      Bekijk cursus
    </a>
  </div>
{% endfor %}
</div>

## Volledig overzicht

Voor een compleet overzicht van alle AI‑opleidingen, ga naar [Cursussen > Overzicht](SCHOLINGSAANBOD.md).

*Laatste update: 18 april 2025*
