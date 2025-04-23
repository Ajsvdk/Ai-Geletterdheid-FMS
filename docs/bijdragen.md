# Voeg  scholing toe

Gebruik onderstaand formulier om nieuwe scholing aan te dragen. De gegevens worden automatisch opgeslagen in deze GitHub-repo als een nieuw issue. Je inzending wordt (voor nu) handmatig verwerkt in het overzicht.

<form id="scholingsformulier">
  <label>Naam van de opleiding:<br><input name="opleiding" required></label><br><br>
  <label>Aanbieder:<br><input name="aanbieder" required></label><br><br>
  <label>Link naar website:<br><input name="link" type="url"></label><br><br>
  <label>Voor wie is het bedoeld?<br><input name="doelgroep"></label><br><br>
  <label>Korte beschrijving:<br><textarea name="beschrijving" rows="5" cols="50"></textarea></label><br><br>
  <label>Jouw naam (optioneel):<br><input name="naam"></label><br><br>
  <button type="submit">Verzenden</button>
</form>

<div id="status" style="margin-top: 1rem;"></div>

<script>
document.getElementById("scholingsformulier").addEventListener("submit", async function(e) {
  e.preventDefault();
  const data = new FormData(e.target);
  const values = Object.fromEntries(data.entries());

  const issueBody = `
**Naam opleiding**: ${values.opleiding}
**Aanbieder**: ${values.aanbieder}
**Website**: ${values.link}
**Doelgroep**: ${values.doelgroep}
**Beschrijving**:
${values.beschrijving}

*Ingediend door: ${values.naam || 'anoniem'}*
  `;

  const response = await fetch("https://api.github.com/repos/Ajsvdk/Ai-Geletterdheid-FMS/issues", {
    method: "POST",
    headers: {
      "Authorization": "Bearer YOUR_TOKEN_HERE",  // ← deze token moet server-side of via Netlify function worden verwerkt
      "Accept": "application/vnd.github+json"
    },
    body: JSON.stringify({
      title: `Nieuw aanbod: ${values.opleiding}`,
      body: issueBody,
      labels: ["inzending"]
    })
  });

  const status = document.getElementById("status");
  if (response.ok) {
    status.innerText = "✅ Bedankt! Je inzending is opgeslagen als issue in de GitHub-repo.";
    e.target.reset();
  } else {
    status.innerText = "❌ Er ging iets mis. Probeer het later opnieuw.";
  }
});
</script>

> *Je inzending wordt zichtbaar op de GitHub-pagina en handmatig verwerkt.*
