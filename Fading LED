void setup()  { 
 pinMode(13,OUTPUT);
} 

void loop()  { 
  // fade in from min to max in increments of 5 points:
  for(int fadeValue = 0 ; fadeValue <= 255; fadeValue +=5) { 
    // sets the value (range from 0 to 255):
    digitalWrite(13, fadeValue);         
    // wait for 30 milliseconds to see the dimming effect    
    delay(100);                            
  } 

  // fade out from max to min in increments of 5 points:
  for(int fadeValue = 255 ; fadeValue >= 0; fadeValue -=5) { 
    // sets the value (range from 0 to 255):
    digitalWrite(13, fadeValue);         
    // wait for 30 milliseconds to see the dimming effect    
    delay(100);                            
  } 
}
