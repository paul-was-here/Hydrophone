// basic code for acquisition of analog data from EMG and conversion to readable voltage value
// no additional data processing
#include <math.h>

void setup() {
  Serial.begin(115000);
}

void loop() {
  float sensorValue = analogRead(A1);
  float voltageValue = sensorValue*5.00/1023.00-2.5;
  Serial.println(voltageValue);
  delayMicroseconds(8);
}
