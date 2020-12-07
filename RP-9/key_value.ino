String receivefromterminal;

void setup() {
Serial.begin(115200);

}

void loop() {

  while ( Serial.available()){

    char karakter = Serial.read();
    Serial.print("char=") ; Serial.println(karakter);

    receivefromterminal+=karakter;
    Serial.print("receivefromterminal=") ; Serial.println(receivefromterminal);    
    
    
   }


}
