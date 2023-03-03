# Codigo Gustavo

#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.iodevices import I2CDevice
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from mindsensorsPYB import mindsensors_i2c, LSA

from time import sleep
from random import randrange

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.D)
right_motor = Motor(Port.B)

# Iniciando o sensor de proximidade
sensor_ultrassonico_direita = UltrasonicSensor(Port.S4)
sensor_ultrassonico_esquerda = UltrasonicSensor(Port.S1)

velocidade_esquerdo = 100
velocidade_direito = 100

while True:
    
    left_motor.run(velocidade_esquerdo)
    right_motor.run(velocidade_direito)
    
    distancia_esquerda = sensor_ultrassonico_esquerda.distance()
    distancia_direita = sensor_ultrassonico_direita.distance()
    
    if distancia_esquerda > 50:
        left_motor.run(-10)
        sleep(0.3)
    if distancia_direita > 50:
        right_motor.run(-10)
        sleep(0.3)