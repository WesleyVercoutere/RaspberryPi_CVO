String receivefromterminal;

void setup() {
Serial.begin(115200);

}

void loop() {

  while ( Serial.available()){

    char karakter = Serial.read();
    Serial.print("char=") ; Serial.println(karakter);

    if (karakter != '\n'){
     receivefromterminal+=karakter;
      Serial.print("receivefromterminal=") ; Serial.println(receivefromterminal);       
      
    }else {

      Serial.println("Bedankt alles goed ontvangen!");      
      Serial.print("receivefromterminal=") ; Serial.println(receivefromterminal);  
      receivefromterminal="";    
    }
   
    
   }


}
