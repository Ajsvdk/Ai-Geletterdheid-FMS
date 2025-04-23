# Voeg een scholing toe

Gebruik onderstaand formulier om nieuwe scholing aan te dragen.  
De gegevens worden automatisch opgeslagen in deze GitHub-repo als een nieuw issue.

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

<div id="status" style="margin-top:1rem;"></div>

<script>
document.getElementById("scholingsformulier").addEventListener("submit", async (e) => {
  e.preventDefault();
  const data = new FormData(e.target);
  const v = Object.fromEntries(data.entries());

  const issueBody = `
**Naam opleiding**: ${v.opleiding}
**Aanbieder**: ${v.aanbieder}
**Website**: ${v.link}
**Doelgroep**: ${v.doelgroep}
**Beschrijving**:
${v.beschrijving}

*Ingediend door: ${v.naam || 'anoniem'}*
  `;

  const r = await fetch("https://api.github.com/repos/Ajsvdk/Ai-Geletterdheid-FMS/issues", {
    method: "POST",
    headers: {
      "Authorization": "Bearer __ISSUE_TOKEN__",    // ← wordt door workflow vervangen
      "Accept": "application/vnd.github+json"
    },
    body: JSON.stringify({
      title: `Nieuw aanbod: ${v.opleiding}`,
      body: issueBody,
      labels: ["inzending"]
    })
  });

  document.getElementById("status").textContent =
    r.ok ? "✅ Bedankt! Je inzending is opgeslagen." :
           "❌ Er ging iets mis. Probeer het later opnieuw.";
  if (r.ok) e.target.reset();
});
</script>
