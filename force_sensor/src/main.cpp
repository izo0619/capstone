#include <Arduino.h>

// put function declarations here:
int sensorToResistance();
enum sensor_type
{
    SQUARE,
    CIRCLE,
    STRIP,
};
float resistanceToForce(enum sensor_type sensor, int resistance);
int sensorValue = 0;
int pin = A0;
const int r = 660;
int r_s = 0;

void setup()
{
    // put your setup code here, to run once:
    Serial.begin(9600);
    analogReadResolution(12);
}

void loop()
{
    int res = sensorToResistance();
    float force = resistanceToForce(sensor_type::SQUARE, res);
    Serial.println(force);
    delay(100);
}

// put function definitions here:
int sensorToResistance()
{
    sensorValue = analogRead(pin);
    // Serial.println(sensorValue); // debugging
    r_s = (1023 - sensorValue) * r / sensorValue;
    // Serial.println(r_s);
    return r_s;
}

float resistanceToForce(enum sensor_type sensor, int resistance)
{
    float force = 0;
    switch (sensor)
    {
    case SQUARE:
        force = pow((resistance / 153.18), (1 / -0.699));
        break;
    case CIRCLE:
        force = pow((resistance / 153.18), (1 / -0.699));
        break;
    case STRIP:
        // todo
        break;
    default:
        break;
    }
    return force;
}
