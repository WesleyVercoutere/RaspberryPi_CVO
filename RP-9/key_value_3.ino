String receivefromterminal;

void setup() {
  Serial.begin(115200);

}

void loop() {

  while ( Serial.available()) {

    char karakter = Serial.read();
    //Serial.print("char=") ; Serial.println(karakter);

    if (karakter != '\n') {
      receivefromterminal += karakter;
      Serial.print("receivefromterminal=") ; Serial.println(receivefromterminal);

    } else {

      Serial.println("Bedankt alles goed ontvangen!");
      Serial.print("receivefromterminal=") ; Serial.println(receivefromterminal);
      int positie_slash = receivefromterminal.indexOf( "/"); // -1 indien niet gevonden
      if (positie_slash >= 0) {
        String key_from_message = receivefromterminal.substring(0, positie_slash); // from => to, from inbegrepen to niet...
        String value_from_message = receivefromterminal.substring(positie_slash + 1);
        Serial.print("key_from_message=") ; Serial.println(key_from_message);
        Serial.print("value_from_message=") ; Serial.println(value_from_message);
      } else {
        Serial.println("Geen geldig key/value pair ontvangen!");
      }

      receivefromterminal = "";
    }


  }


}
