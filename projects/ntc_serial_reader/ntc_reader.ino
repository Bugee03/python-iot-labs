/*
  NTC Thermistor Reader for Arduino Mega 2560
  Circuit:
    VCC (5V) ---> [ R_REF (10k) ] ---> Pin A0 ---> [ NTC Thermistor ] ---> GND
*/

const int NTC_PIN = A0;

// Hardware & Thermistor Parameters
const float R_REF = 10000.0;     // Pull-up resistor connected to VCC (10k Ohm)
const float R_25 = 10000.0;      // NTC nominal resistance at 25 deg C (10k Ohm)
const float BETA = 3950.0;       // Beta coefficient (B25/85 or B25/100, typically 3950)
const float T_25 = 298.15;       // 25 deg C in Kelvin
const float ADC_MAX = 1023.0;    // 10-bit ADC maximum value for ATmega2560

void setup() {
  Serial.begin(115200);
  while (!Serial) {
    ; // Wait for serial connection
  }
}

void loop() {
  int adcValue = analogRead(NTC_PIN);
  float voltage = (adcValue * 5.0) / ADC_MAX;

  float resistance = 0.0;
  float tempC = 0.0;

  // With NTC connected between A0 and GND, and R_REF pull-up to VCC:
  // R_ntc = R_ref * (ADC / (ADC_max - ADC))
  if (adcValue > 0 && adcValue < (int)ADC_MAX) {
    resistance = R_REF * ((float)adcValue / (ADC_MAX - (float)adcValue));

    // Beta equation: 1/T_K = 1/T_25 + (1/BETA) * ln(R / R_25)
    float steinhart = log(resistance / R_25);
    steinhart /= BETA;
    steinhart += 1.0 / T_25;
    float tempK = 1.0 / steinhart;
    tempC = tempK - 273.15;
  }

  // Send clean JSON output
  Serial.print("{\"adc\":");
  Serial.print(adcValue);
  Serial.print(",\"voltage\":");
  Serial.print(voltage, 3);
  Serial.print(",\"resistance\":");
  Serial.print(resistance, 1);
  Serial.print(",\"temp_c\":");
  Serial.print(tempC, 2);
  Serial.println("}");

  delay(500);
}
