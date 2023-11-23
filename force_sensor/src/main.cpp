#include <Arduino.h>

const int r = 3300;
int r_s = 0;
const int numSensors = 9;
int sensorPins[numSensors] = {36, 39, 34, 35, 32, 33, 25, 26, 27};
int sensorValues[numSensors] = {0, 0, 0, 0, 0, 0, 0, 0, 0};

void setup()
{
    Serial.begin(9600);
    analogReadResolution(12);
}

void printAllSensors()
{
    Serial.print(millis());
    Serial.print(", ");
    for (int i = 0; i < numSensors; i++)
    {
        Serial.print(sensorValues[i]);
        if (i < numSensors - 1)
        {
            Serial.print(", ");
        }
    }
    Serial.println();
}

int sensorToResistance(int pin)
{
    int sensorValue = analogRead(pin);
    if (sensorValue == 0)
    {
        return 0;
    }
    r_s = (4095 - sensorValue) * r / sensorValue;
    return r_s;
}

float resistanceToForce(int resistance)
{
    float force = 0;
    if (resistance == 0)
    {
        return 0;
    }

    force = pow((resistance / (153.18 * 1000)), (1 / -0.699));
    return force;
}

void readAllSensors()
{
    for (int i = 0; i < numSensors; i++)
    {
        int res = sensorToResistance(sensorPins[i]);
        float force = resistanceToForce(res);
        sensorValues[i] = force;
    }
}

void loop()
{
    readAllSensors();
    printAllSensors();
    delay(10);
}
