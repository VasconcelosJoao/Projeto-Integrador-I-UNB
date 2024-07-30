// Sensores
const int sensorLeft = 11;   // sensor da esquerda
const int sensorCenter = 12; // sensor do meio
const int sensorRight = 13;  // sensor da direita

// Motores
const int motorLeftSpeed = 5;      // pino de velocidade do motor da esquerda
const int motorLeftDirection = 6;  // pino de direção do motor da esquerda
const int motorRightSpeed = 10;    // pino de velocidade do motor da direita
const int motorRightDirection = 9; // pino de direção do motor da direita

volatile int sensorStateLeft;
volatile int sensorStateCenter;
volatile int sensorStateRight;

void setup()
{
  Serial.begin(9600);

  pinMode(motorLeftSpeed, OUTPUT);
  digitalWrite(motorLeftDirection, LOW);
  pinMode(motorRightSpeed, OUTPUT);
  digitalWrite(motorRightDirection, LOW);

  pinMode(sensorLeft, INPUT);
  pinMode(sensorCenter, INPUT);
  pinMode(sensorRight, INPUT);
}

void loop()
{
  controlador();
}


void readSensorT()
{
  sensorStateLeft = digitalRead(sensorLeft);
  sensorStateCenter = digitalRead(sensorCenter);
  sensorStateRight = digitalRead(sensorRight);
}

void controlador()
{
  readSensorT();
  if (sensorStateLeft == 1 && sensorStateCenter == 0 && sensorStateRight == 1)
  {
    analogWrite(motorLeftSpeed, 52);
    analogWrite(motorRightSpeed, 47);
  }
  else if (sensorStateLeft == 0 && sensorStateRight == 1)
  {
    analogWrite(motorLeftSpeed, 0);
    analogWrite(motorRightSpeed, 45);
    do
    {
      readSensorT();
    } while (sensorStateLeft == 1 && sensorStateCenter == 0 && sensorStateRight == 1);
  }
  else if (sensorStateLeft == 1 && sensorStateRight == 0)
  {
    analogWrite(motorLeftSpeed, 50);
    analogWrite(motorRightSpeed, 0);
    do
    {
      readSensorT();
    } while (sensorStateLeft == 1 && sensorStateCenter == 0 && sensorStateRight == 1);
  }
}