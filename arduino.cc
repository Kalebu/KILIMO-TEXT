int moisture_sensor = A1;
int pump = 12;
float moisture_concentration;
int limit_concentration = 10;
byte signal;

int signal_check(){
    byte n = 0;  
   if (Serial.available()){
           n   = Serial.read();
           return n;
   }
   return n;
}
  

void setup(){
  
  Serial.begin(9600);
  pinMode(pump, OUTPUT);
  pinMode(moisture_sensor, INPUT);
}


void loop(){
  signal = signal_check();
  moisture_concentration = analogRead(moisture_sensor);
  //Serial.println(moisture_concentration);
  //byte received_signal = signal_check()  
  if (moisture_concentration>limit_concentration){
       digitalWrite(pump, HIGH);
       moisture_concentration = (moisture_concentration/1024)*255;
       if (signal!=0){
         moisture_concentration = signal;
       }
        byte value =(byte)moisture_concentration;
       Serial.write(value);
       delay(1000);
  }
}
 
