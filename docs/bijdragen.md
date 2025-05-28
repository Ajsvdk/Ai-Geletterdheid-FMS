# Voeg een scholing toe

Gebruik onderstaand formulier om nieuwe AI-scholingsmogelijkheden aan te dragen.  
De gegevens worden automatisch opgeslagen in deze GitHub-repo als een nieuw issue.

<form id="scholingsformulier">
  <div class="form-group">
    <label for="aanbieder">Aanbieder*:</label>
    <input name="aanbieder" id="aanbieder" required placeholder="Bijv. Radboudumc, HarvardX">
  </div>

  <div class="form-group">
    <label for="title">Titel van de opleiding*:</label>
    <input name="title" id="title" required placeholder="Bijv. AI in de klinische praktijk">
  </div>

  <div class="form-group">
    <label for="doelgroep">Doelgroep (Specialisme)*:</label>
    <select name="doelgroep" id="doelgroep" required>
      <option value="">Selecteer een specialisme</option>
      <option value="Alle specialismen">Alle specialismen</option>
      <option value="Allergologie">Allergologie</option>
      <option value="Anesthesiologie">Anesthesiologie</option>
      <option value="Cardiologie">Cardiologie</option>
      <option value="Dermatologie en Venereologie">Dermatologie en Venereologie</option>
      <option value="Heelkunde">Heelkunde</option>
      <option value="Interne Geneeskunde">Interne Geneeskunde</option>
      <option value="Keel-, Neus- en Oorheelkunde">Keel-, Neus- en Oorheelkunde</option>
      <option value="Kindergeneeskunde">Kindergeneeskunde</option>
      <option value="Klinisch Chemici">Klinisch Chemici</option>
      <option value="Klinisch Fysici">Klinisch Fysici</option>
      <option value="Klinische Genetica">Klinische Genetica</option>
      <option value="Klinische Geriatrie">Klinische Geriatrie</option>
      <option value="Longziekten en Tuberculose">Longziekten en Tuberculose</option>
      <option value="Maag, Darm en Lever">Maag, Darm en Lever</option>
      <option value="Medische Microbiologie">Medische Microbiologie</option>
      <option value="Intensive Care">Intensive Care</option>
      <option value="Neurochirurgie">Neurochirurgie</option>
      <option value="Neurologie">Neurologie</option>
      <option value="Nucleaire Geneeskunde">Nucleaire Geneeskunde</option>
      <option value="Obstetrie en Gynaecologie">Obstetrie en Gynaecologie</option>
      <option value="Oogheelkunde">Oogheelkunde</option>
      <option value="Orthopedie">Orthopedie</option>
      <option value="Pathologie">Pathologie</option>
      <option value="Plastische Chirurgie">Plastische Chirurgie</option>
      <option value="Psychiatrie">Psychiatrie</option>
      <option value="Radiologie">Radiologie</option>
      <option value="Radiotherapie en Oncologie">Radiotherapie en Oncologie</option>
      <option value="Reumatologie">Reumatologie</option>
      <option value="Revalidatiegeneeskunde">Revalidatiegeneeskunde</option>
      <option value="Sportgeneeskunde">Sportgeneeskunde</option>
      <option value="Thoraxchirurgie">Thoraxchirurgie</option>
      <option value="Urologie">Urologie</option>
      <option value="Ziekenhuisfarmacie">Ziekenhuisfarmacie</option>
      <option value="Ziekenhuisgeneeskunde">Ziekenhuisgeneeskunde</option>
    </select>
  </div>

  <div class="form-group">
    <label for="tijdsduur">Tijdsduur:</label>
    <input name="tijdsduur" id="tijdsduur" placeholder="Bijv. 4 uur, 2 dagen, 6 weken">
  </div>

  <div class="form-group">
    <label for="kosten">Kosten:</label>
    <input name="kosten" id="kosten" placeholder="Bijv. Gratis, €495, €2500">
  </div>

  <button type="submit">Verzenden</button>
</form>

<div id="status" style="margin-top:1rem;"></div>

<style>
.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  font-size: 1rem;
}

.form-group input:focus,
.form-group select:focus {
  outline: none;
  border-color: var(--md-primary-fg-color);
  box-shadow: 0 0 0 2px var(--md-primary-fg-color--light);
}

button[type="submit"] {
  background-color: var(--md-primary-fg-color);
  color: white;
  padding: 0.75rem 2rem;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s;
}

button[type="submit"]:hover {
  background-color: var(--md-primary-fg-color--dark);
}

#status {
  padding: 1rem;
  border-radius: 4px;
  font-weight: 600;
}

#status.success {
  background-color: #e8f5e9;
  color: #2e7d32;
}

#status.error {
  background-color: #ffebee;
  color: #c62828;
}
</style>

<script>
document.getElementById("scholingsformulier").addEventListener("submit", async (e) => {
  e.preventDefault();
  const data = new FormData(e.target);
  const v = Object.fromEntries(data.entries());

  const issueBody = `
## Nieuwe AI-opleiding ingediend

**Aanbieder**: ${v.aanbieder}
**Titel**: ${v.title}
**Doelgroep**: ${v.doelgroep}
**Tijdsduur**: ${v.tijdsduur || 'Niet opgegeven'}
**Kosten**: ${v.kosten || 'Niet opgegeven'}

---
Deze inzending moet worden toegevoegd aan het scholingsaanbod.
  `;

  const statusEl = document.getElementById("status");
  statusEl.textContent = "Verzenden...";
  statusEl.className = "";

  try {
    const r = await fetch("https://api.github.com/repos/Ajsvdk/Ai-Geletterdheid-FMS/issues", {
      method: "POST",
      headers: {
        "Authorization": "Bearer __ISSUE_TOKEN__",    // ← wordt door workflow vervangen
        "Accept": "application/vnd.github+json"
      },
      body: JSON.stringify({
        title: `Nieuwe opleiding: ${v.title}`,
        body: issueBody,
        labels: ["nieuwe-opleiding"]
      })
    });

    if (r.ok) {
      statusEl.textContent = "✅ Bedankt! Je inzending is opgeslagen en wordt binnenkort verwerkt.";
      statusEl.className = "success";
      e.target.reset();
    } else {
      throw new Error("Verzenden mislukt");
    }
  } catch (error) {
    statusEl.textContent = "❌ Er ging iets mis. Probeer het later opnieuw of neem contact op.";
    statusEl.className = "error";
  }
});
</script>
