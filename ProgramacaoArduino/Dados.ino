#include <SD.h>
#include <SPI.h>


#define CS_PIN 10 // Defina para o pino CS do seu módulo SD
#define ACS712_PIN A0 // Pino analógico conectado ao ACS712
#define D_Sensor_Left 3
#define D_Sensor_Right 2

volatile double velocity_Left = 0;
volatile double velocity_Right = 0;
volatile long prevT_Left = 0;
volatile long prevT_Right = 0;
unsigned long lastPrintTime = 0;
const unsigned long printInterval = 100;
const unsigned long timeoutInterval = 500; // Ajuste conforme necessário


void setup() {
  Serial.begin(115200);
  pinMode(CS_PIN, OUTPUT);

  if (!SD.begin(CS_PIN)) {
    Serial.println("Falha na inicialização do cartão SD");
    return;
  }

  attachInterrupt(digitalPinToInterrupt(D_Sensor_Left), readEncoderLeft, RISING);
  attachInterrupt(digitalPinToInterrupt(D_Sensor_Right), readEncoderRight, RISING);
}

void loop() {
  rpm();
  logDataToSD(); // Chama a função para registrar os dados no SD
}


// float readCurrent() {
//   int sensorValue = analogRead(ACS712_PIN);
//   float voltage = (sensorValue / 1023.0) * 5.0; // Converte o valor lido para tensão
//   float current = (voltage - 2.5) / 0.185; // Ajuste 0.185 para a sensibilidade do seu sensor
//   return current;
// }

void logDataToSD() {
  float current = analogRead(ACS712_PIN);
  String dataString = String(millis()) + "," + String(velocity_Left / 20.0 * 60.0) + "," + String(velocity_Right / 20.0 * 60.0) + "," + String(current);

  bool exists = SD.exists("datalog.csv");
  File dataFile = SD.open("datalog.csv", FILE_WRITE);

  if (dataFile) {
    if (!exists) {
      dataFile.println("tempo,rpmEsquerdo,rpmDireito,corrente");
    }
    dataFile.println(dataString);
    dataFile.close();
    Serial.println("Dados gravados: " + dataString);
  } else {
    Serial.println("Erro ao abrir o arquivo datalog.csv");
  }
}

void readEncoderLeft()
{
  long currT = micros();
  double deltaT = ((double)(currT - prevT_Left)) / 1.0e6;
  if (deltaT >= 0.015)
  {
    velocity_Left = 1 / deltaT;
    prevT_Left = currT;
  }
}

void readEncoderRight()
{
  long currT = micros();
  double deltaT = ((double)(currT - prevT_Right)) / 1.0e6;
  if (deltaT >= 0.015)
  {
    velocity_Right = 1 / deltaT;
    prevT_Right = currT;
  }
}

void rpm()
{
  unsigned long currentMillis = millis();
  if (currentMillis - lastPrintTime >= printInterval)
  {
    lastPrintTime = currentMillis;
    if (currentMillis - (prevT_Left / 1000) > timeoutInterval)
    {
      velocity_Left = 0;
    }
    if (currentMillis - (prevT_Right / 1000) > timeoutInterval)
    {
      velocity_Right = 0;
    }
  }
}