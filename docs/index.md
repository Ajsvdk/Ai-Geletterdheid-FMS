{% include "includes/top_nav.html" %}

# Scholingsaanbod AI

*Laatste update: 18 april 2025*

Voorlopgie open-source, toegankelijke en bijwerkbaar uitwerking van AI-onderwijs voor zorgmedewerkers, in het bijzonder artsen.


## Aanbevolen cursussen

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 px-4">
{% for c in courses %}
  <div class="card p-4 shadow-lg rounded-lg">
    <h3 class="text-xl font-bold">{{ c['Titel'] }}</h3>
    <p class="text-gray-600">{{ c['Aanbieder'] }}</p>
    <p class="mt-2 font-semibold">{{ c['Kosten'] }}</p>
    <a href="{{ c['Link'] }}" class="mt-4 inline-block px-4 py-2 bg-primary text-white rounded">
      Bekijk cursus
    </a>
  </div>
{% endfor %}
</div>

## Volledig overzicht

Voor een compleet overzicht van alle AI‑opleidingen, ga naar [Cursussen > Overzicht](SCHOLINGSAANBOD.md).
