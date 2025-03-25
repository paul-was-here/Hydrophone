#include <math.h>

void setup() {
  Serial.begin(115000);
}

void loop() {
  int sensorValue = analogRead(A1);
  int voltageValue = ((sensorValue*5000L) / 1023) - 2500;
  Serial.write((uint8_t*)&voltageValue, sizeof(voltageValue));
  delayMicroseconds(200);
}
