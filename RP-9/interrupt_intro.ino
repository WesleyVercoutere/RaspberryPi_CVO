// https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/

const byte ledPin = 13;
const byte interruptPin = 2;
volatile byte state = LOW;
byte state_before=0;

void blink() {
  state = !state;
}

void setup() {
  Serial.begin(500000);
  pinMode(ledPin, OUTPUT);
  pinMode(interruptPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(interruptPin), blink, CHANGE);
}

void loop() {
  if (state_before != state){
    state_before = state;
    digitalWrite(ledPin, state);
    Serial.print("state");Serial.println(state);
  }

}
