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

def gera_num_aleatorio(y):
    # a função não está dando um retorno para y = 1
    if y == 1:
        return 0
    
    x = randrange(y)
    return x

def avanca():
    sleep(1)
    potencia_esquerdo = 200
    potencia_direito = 200

def giro_direita():
    sleep(1)
    while (giro.angle() < 85):
        motor_esquerdo.run(100)
        motor_direito.run(0)
    giro.reset_angle(0)

def giro_esquerda():
    sleep(1)
    while (giro.angle() > -85):
        motor_esquerdo.run(0)
        motor_direito.run(150)
    giro.reset_angle(0)

def volta():
    # ao encontrar a cor preta ele deve girar 180º e retornar
    while (giro.angle() < 175):
        motor_esquerdo.run(150)
        motor_direito.run(0)
    giro.reset_angle(0)

def reset(angulo_a_voltar):
    # ao voltar de uma cor preta para uma cor não preta, o robo deve retornar a
    # angulação inicial
    if angulo_a_voltar > 0:
        giro_direita()
    else:
        giro_esquerda()

# Objetos 
ev3dev = EV3Brick()

motor_esquerdo = Motor(Port.B)
motor_direito = Motor(Port.C)

#sensor_luzes = LSA(Port.S1)
giro = GyroSensor(Port.S4)
sensor_cor = ColorSensor(Port.S1) # Usar um sensor por enquanto.

# constantes para ajustes finos
potencia_base = 180
kp_externo = 2.5
kp_interno = 1.5

# constantes atuais
potencia_esquerdo = 200
potencia_direito = 200

# setada no angulo do gyro
giro.reset_angle(0)

# iniciando as várias opções das cores
opcoes_azul = [giro_direita, giro_esquerda, avanca]
opcoes_vermelho = [giro_direita, giro_esquerda, avanca]

# dicionário de uso para reajuste no angulo após um erro (ler o preto)
dicionario_acao_angulo = {giro_direita: 90, giro_esquerda: -90}

# armazena as funções corretas para cada cor
funcoes_cores = {Color.BLUE: '', Color.RED: '', Color.GREEN: ''}

cor_anterior = ''
erro = False
qtde_possivel_num_aleatorio = 3
while True:
    ev3dev.speaker.beep()
    num_aleatorio = gera_num_aleatorio(qtde_possivel_num_aleatorio)
    
    motor_esquerdo.run(potencia_esquerdo)
    motor_direito.run(potencia_direito)
    
    sleep(2)
    if (sensor_cor.color() == Color.RED):
        if erro:
            # reseta para a angulação inicial
            if acao_tomada == avanca:
                volta()
            else:
                reset(dicionario_acao_angulo[acao_tomada])
                
        if (len(opcoes_vermelho) == 1): # achou a função correta por eliminação
            funcoes_cores[Color.RED] = opcoes_vermelho[0]
            funcoes_cores[Color.RED]()
        else:
            # testar aleatoriamente uma nova ação
            acao_tomada = opcoes_vermelho[num_aleatorio]
            acao_tomada()
        
        cor_anterior = Color.RED
        erro = False
            
    if (sensor_cor.color() == Color.BLUE):
        cor_anterior = Color.BLUE
        erro = False
        lista_funcoes[num_aleatorio]()
        
    if (sensor_cor.color() == Color.BLACK):
        
        opcoes_vermelho.remove(acao_tomada)
        qtde_possivel_num_aleatorio -= 1
        volta()
        
        cor_anterior = Color.BLACK
        erro = True
     
'''
while True:
    # a = [sensor_luzes.ReadRaw_Uncalibrated()[4], sensor_luzes.ReadRaw_Uncalibrated()[5]]
    
    sensor_direito_ext = sensor_luzes.ReadRaw_Calibrated()[7]
    sensor_esquerdo_ext = sensor_luzes.ReadRaw_Calibrated()[0]
    #sensor_direito_ext = 0
    #sensor_esquerdo_ext = 0
    
    sensor_direito_int = sensor_luzes.ReadRaw_Calibrated()[4]
    sensor_esquerdo_int = sensor_luzes.ReadRaw_Calibrated()[3]
    
    diff_externos = - (sensor_direito_ext - sensor_esquerdo_ext)
    
    """
    A diferença dos sensores internos eh esq - dir por que ele pega em cima da linha preta
    diferentemente dos sensores mais externos que pegam na superficie branca. Assim sendo,
    a correção eh invertida
    """
    diff_internos = sensor_esquerdo_int - sensor_direito_int
    
    potencia_esquerdo = potencia_base - (kp_externo * diff_externos) - (kp_externo * diff_internos)
    potencia_direito = potencia_base + (kp_externo * diff_externos) + (kp_externo * diff_internos)
    
    motor_esquerdo.run(potencia_esquerdo)
    motor_direito.run(potencia_direito)
'''

