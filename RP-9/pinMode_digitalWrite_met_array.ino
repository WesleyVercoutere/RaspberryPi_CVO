// Gebruik van arrays om verschillende pinnen als output te definieren en te sturen

int pins[4] = {5, 6, 7, 8};

void setup() {

  for (int i = 0; i < 4 ; i++) {
    pinMode(pins[i], OUTPUT);
  }

}

void loop() {

  for (int i = 0; i < 4 ; i++) {
    digitalWrite(pins[i], HIGH);
    delay(500);
    digitalWrite(pins[i], LOW);
    delay(500);
  }

}
