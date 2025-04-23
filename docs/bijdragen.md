# Voeg een scholing toe

Vul het onderstaande formulier in om een nieuwe AI-scholing aan te dragen. Deze gegevens worden (voor nu) niet automatisch opgeslagen — kopieer en mail ze handmatig naar de redactie.

<form name="submit-to-google-sheet">
  <label for="opleiding">Naam van de opleiding:</label><br>
  <input type="text" id="opleiding" name="opleiding" required><br><br>

  <label for="aanbieder">Aanbieder:</label><br>
  <input type="text" id="aanbieder" name="aanbieder" required><br><br>

  <label for="link">Link naar website:</label><br>
  <input type="url" id="link" name="link"><br><br>

  <label for="doelgroep">Voor wie is het bedoeld?</label><br>
  <input type="text" id="doelgroep" name="doelgroep"><br><br>

  <label for="beschrijving">Korte beschrijving:</label><br>
  <textarea id="beschrijving" name="beschrijving" rows="5" cols="40"></textarea><br><br>

  <label for="naam">Jouw naam (optioneel):</label><br>
  <input type="text" id="naam" name="naam"><br><br>

  <button type="submit">Verzenden</button>
</form>

<script>
  const form = document.querySelector("form");
  form.addEventListener("submit", function(e) {
    e.preventDefault();
    alert("Dank je! Kopieer je ingevulde gegevens en mail ze naar de redactie.");
  });
</script>
