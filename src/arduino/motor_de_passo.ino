#include <AccelStepper.h>

#define STEP_ESQ 2
#define DIR_ESQ 3

#define STEP_DIR 4
#define DIR_DIR 5

#define ENABLE_PIN 8

AccelStepper motorEsq(AccelStepper::DRIVER, STEP_ESQ, DIR_ESQ);
AccelStepper motorDir(AccelStepper::DRIVER, STEP_DIR, DIR_DIR);

void setup() {
  Serial.begin(9600);

  pinMode(ENABLE_PIN, OUTPUT);
  digitalWrite(ENABLE_PIN, LOW); // LOW ativa o A4988

  motorEsq.setMaxSpeed(800);
  motorEsq.setAcceleration(400);

  motorDir.setMaxSpeed(800);
  motorDir.setAcceleration(400);

  Serial.println("Pronto");
}

void loop() {
  if (Serial.available()) {
    int passosEsq = Serial.parseInt();
    int passosDir = Serial.parseInt();

    motorEsq.move(passosEsq);
    motorDir.move(passosDir);
  }

  motorEsq.run();
  motorDir.run();
}