# Voeg onderwijsaanbod toe

Gebruik onderstaand formulier nieuwe scholing aan te dragen. De gegevens worden automatisch opgeslagen in deze GitHub-repo als een nieuw issue. Je inzending wordt (voor nu) handmatig verwerkt in het overzicht.

<form id="scholingsformulier">
  <div class="form-group">
    <label for="opleiding">Naam van de opleiding:</label>
    <input name="opleiding" id="opleiding" required>
  </div>

  <div class="form-group">
    <label for="aanbieder">Aanbieder:</label>
    <input name="aanbieder" id="aanbieder" required>
  </div>

  <div class="form-group">
    <label for="link">Link naar website:</label>
    <input name="link" id="link" type="text" placeholder="https://voorbeeld.nl">
  </div>

  <div class="form-group">
    <label for="doelgroep">Voor wie is het bedoeld?</label>
    <input name="doelgroep" id="doelgroep">
  </div>

  <div class="form-group">
    <label for="beschrijving">Korte beschrijving:</label>
    <textarea name="beschrijving" id="beschrijving" rows="5"></textarea>
  </div>

  <div class="form-group">
    <label for="naam">Jouw naam (optioneel):</label>
    <input name="naam" id="naam">
  </div>

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
      "Authorization": "Bearer YOUR_TOKEN_HERE",  // ← vervang met veilige token via backend
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
