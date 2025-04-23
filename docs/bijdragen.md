# Voeg een scholing toe

Gebruik onderstaand formulier om een nieuwe scholing aan te dragen. De gegevens worden automatisch opgeslagen in de GitHub-repo als een nieuw issue.

<form id="scholingsformulier">
  <label>Naam van de opleiding:<br><input name="opleiding" required></label><br><br>
  <label>Aanbieder:<br><input name="aanbieder" required></label><br><br>
  <label>Link naar website:<br><input name="link"></label><br><br>
  <label>Doelgroep:<br><input name="doelgroep"></label><br><br>
  <label>Korte beschrijving:<br><textarea name="beschrijving" rows="5" cols="50"></textarea></label><br><br>
  <label>Jouw naam (optioneel):<br><input name="naam"></label><br><br>
  <button type="submit">Verstuur</button>
</form>

<div id="status"></div>

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

  const response = await fetch("https://api.github.com/repos/YOUR-USERNAME/YOUR-REPO/issues", {
    method: "POST",
    headers: {
      "Authorization": "Bearer {{ site.token }}",
      "Accept": "application/vnd.github+json"
    },
    body: JSON.stringify({
      title: `Nieuw aanbod: ${values.opleiding}`,
      body: issueBody,
