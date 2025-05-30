# Bijdragen aan het AI Scholingsaanbod

Help mee dit overzicht actueel en compleet te houden door nieuwe AI-scholingsmogelijkheden toe te voegen.

## 🆕 Nieuwe scholing toevoegen

Vul het onderstaande formulier in om een nieuwe AI-scholing toe te voegen aan het overzicht:

<form action="https://formspree.io/f/mpwraqgp" method="POST" style="max-width: 600px; margin: 0 auto;">
  <input type="hidden" name="_subject" value="Nieuwe AI Scholing: [SCHOLING]" />
  <input type="hidden" name="_next" value="https://ajsvdk.github.io/Ai-Geletterdheid-FMS/bijdragen/?success=true" />
  
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

  <button type="submit" style="background-color: #009688; color: white; padding: 12px 24px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; width: 100%;">
    📧 Scholing Indienen
  </button>
</form>

<script>
// Check for success parameter in URL
const urlParams = new URLSearchParams(window.location.search);
if (urlParams.get('success') === 'true') {
    document.body.insertAdjacentHTML('afterbegin', 
        '<div style="background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; padding: 15px; margin: 20px auto; border-radius: 5px; max-width: 600px; text-align: center;">' +
        '✅ <strong>Bedankt!</strong> Je scholing is succesvol ingediend en wordt binnenkort gecontroleerd.' +
        '</div>'
    );
}
</script>

---

## ❓ Vragen of problemen?

Voor bugs, verbeteringen of andere vragen: **📧 [aionderwijszorg@gmail.com](mailto:aionderwijszorg@gmail.com)**

---

*Alle bijdragen worden gecontroleerd op relevantie en kwaliteit voordat ze worden toegevoegd aan het overzicht.*
