/*
Communication Parameters:
8 Data, 1 Stop, No Parity
Baud rate : 9600 
Commands:
OFF command: FF 01 00 (HEX) or 255 1 0 (DEC)
ON command: FF 01 01 (HEX) or 255 1 1 (DEC)
*/
long incommingCommand = 0;
int incomingByte = 0;   // for incoming serial data
 
void setup() {
        Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
        pinMode(6, OUTPUT);
}
 
void loop() {
 
        if (Serial.available() > 0) {

                incomingByte = Serial.read();

                if(incomingByte == 255)
                {
                  digitalWrite(6, HIGH);
                }
                else if(incomingByte == 100)
                {
                  digitalWrite(6, LOW);
                }

// For use with BackyardNikon
//
//                if(incomingByte == 255)
//                {
//                  digitalWrite(6, HIGH);
//                }
// 
//                if (incomingByte==255) incommingCommand = 0;
//                
//                incommingCommand = incommingCommand*256;
//                incommingCommand  = incommingCommand + incomingByte;
//                
//                if (incommingCommand == 16711936)                    //alumer
//                  digitalWrite(6, HIGH);
// 
//                if (incommingCommand == 16711937)                    //éteindre
//                  digitalWrite(6, LOW);
// 
        }

}
