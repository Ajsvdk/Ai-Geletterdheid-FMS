# Bijdragen aan het AI Scholingsaanbod

Help mee dit overzicht actueel en compleet te houden door nieuwe AI-scholingsmogelijkheden toe te voegen.

## 🆕 Nieuwe scholing toevoegen

Vul het onderstaande formulier in om een nieuwe AI-scholing toe te voegen aan het overzicht:

<form id="course-form" style="max-width: 600px; margin: 0 auto;">
  <div style="margin-bottom: 20px;">
    <label for="aanbieder" style="display: block; margin-bottom: 5px; font-weight: bold;">Aanbieder *</label>
    <input type="text" id="aanbieder" name="aanbieder" required style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
  </div>

  <div style="margin-bottom: 20px;">
    <label for="titel" style="display: block; margin-bottom: 5px; font-weight: bold;">Titel van de scholing *</label>
    <input type="text" id="titel" name="titel" required style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
  </div>

  <div style="margin-bottom: 20px;">
    <label for="doelgroep" style="display: block; margin-bottom: 5px; font-weight: bold;">Doelgroep/Specialisme *</label>
    <select id="doelgroep" name="doelgroep" required style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
      <option value="">Selecteer specialisme...</option>
      <option value="Algemeen">Algemeen (alle zorgprofessionals)</option>
      <option value="Allergologie">Allergologie</option>
      <option value="Anesthesiologie">Anesthesiologie</option>
      <option value="Cardiologie">Cardiologie</option>
      <option value="Cardiothoracale chirurgie">Cardiothoracale chirurgie</option>
      <option value="Dermatologie">Dermatologie</option>
      <option value="Gynaecologie">Gynaecologie</option>
      <option value="Heelkunde">Heelkunde</option>
      <option value="Interne geneeskunde">Interne geneeskunde</option>
      <option value="Klinische chemie">Klinische chemie</option>
      <option value="Neurologie">Neurologie</option>
      <option value="Oncologie">Oncologie</option>
      <option value="Radiologie">Radiologie</option>
      <option value="Radiotherapie en Oncologie">Radiotherapie en Oncologie</option>
      <option value="Verpleegkunde">Verpleegkunde</option>
      <option value="Overig">Overig</option>
    </select> 
  </div>

  <div style="margin-bottom: 20px;">
    <label for="tijdsduur" style="display: block; margin-bottom: 5px; font-weight: bold;">Tijdsduur</label>
    <input type="text" id="tijdsduur" name="tijdsduur" placeholder="bijv. 2 dagen, 4 uur, etc." style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
  </div>

  <div style="margin-bottom: 20px;">
    <label for="kosten" style="display: block; margin-bottom: 5px; font-weight: bold;">Kosten</label>
    <input type="text" id="kosten" name="kosten" placeholder="bijv. Gratis, €500, etc." style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
  </div>

  <div style="margin-bottom: 20px;">
    <label for="website" style="display: block; margin-bottom: 5px; font-weight: bold;">Website/Link</label>
    <input type="text" id="website" name="website" placeholder="Website URL (optioneel)" style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
  </div>

  <div style="margin-bottom: 20px;">
    <label for="beschrijving" style="display: block; margin-bottom: 5px; font-weight: bold;">Korte beschrijving</label>
    <textarea id="beschrijving" name="beschrijving" rows="4" placeholder="Korte beschrijving van de scholing..." style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"></textarea>
  </div>

  <div style="margin-bottom: 20px;">
    <label for="aanvullende-info" style="display: block; margin-bottom: 5px; font-weight: bold;">Aanvullende informatie</label>
    <textarea id="aanvullende-info" name="aanvullende-info" rows="3" placeholder="Andere relevante informatie (vereisten, certificering, etc.)" style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"></textarea>
  </div>

  <button type="submit" id="submit-btn" style="background-color: #009688; color: white; padding: 12px 24px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; width: 100%;">
    ✅ Scholing Toevoegen
  </button>
  
  <div id="form-status" style="margin-top: 15px; padding: 10px; border-radius: 4px; display: none;"></div>
</form>

<script>
document.getElementById('course-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const submitBtn = document.getElementById('submit-btn');
    const statusDiv = document.getElementById('form-status');
    
    // Disable button and show loading
    submitBtn.disabled = true;
    submitBtn.innerHTML = '⏳ Bezig met verzenden...';
    statusDiv.style.display = 'none';
    
    // Get form data
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData);
    
    // Create issue body
    const issueBody = `**Aanbieder**
${data.aanbieder}

**Titel van de scholing**
${data.titel}

**Doelgroep/Specialisme**
${data.doelgroep}

**Tijdsduur**
${data.tijdsduur || 'Niet opgegeven'}

**Kosten**
${data.kosten || 'Niet opgegeven'}

**Website/Link**
${data.website || 'Niet opgegeven'}

**Beschrijving**
${data.beschrijving || 'Niet opgegeven'}

**Aanvullende informatie**
${data['aanvullende-info'] || 'Niet opgegeven'}

---
*Automatisch ingediend via het website formulier*`;

    try {
        // Submit to GitHub Issues API
        const response = await fetch('https://api.github.com/repos/Ajsvdk/Ai-Geletterdheid-FMS/issues', {
            method: 'POST',
            headers: {
                'Accept': 'application/vnd.github+json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title: `[SCHOLING] ${data.titel} - ${data.aanbieder}`,
                body: issueBody,
                labels: ['nieuwe-scholing']
            })
        });

        if (response.ok) {
            // Success
            statusDiv.innerHTML = '✅ <strong>Bedankt!</strong> Je scholing is succesvol ingediend en wordt binnenkort gecontroleerd.';
            statusDiv.style.display = 'block';
            statusDiv.style.backgroundColor = '#d4edda';
            statusDiv.style.color = '#155724';
            statusDiv.style.border = '1px solid #c3e6cb';
            
            // Reset form
            e.target.reset();
        } else {
            throw new Error('Failed to submit');
        }
    } catch (error) {
        // Error - fallback to email
        statusDiv.innerHTML = '⚠️ <strong>Probleem bij verzenden.</strong> Stuur je gegevens naar <a href="mailto:aionderwijszorg@gmail.com">aionderwijszorg@gmail.com</a>';
        statusDiv.style.display = 'block';
        statusDiv.style.backgroundColor = '#fff3cd';
        statusDiv.style.color = '#856404';
        statusDiv.style.border = '1px solid #ffeaa7';
    } finally {
        // Re-enable button
        submitBtn.disabled = false;
        submitBtn.innerHTML = '✅ Scholing Toevoegen';
    }
});
</script>

---

## ❓ Vragen of problemen?

Voor bugs, verbeteringen of andere vragen: **📧 [aionderwijszorg@gmail.com](mailto:aionderwijszorg@gmail.com)**

---

*Alle bijdragen worden gecontroleerd op relevantie en kwaliteit voordat ze worden toegevoegd aan het overzicht.*
