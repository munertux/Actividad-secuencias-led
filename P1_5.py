from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau
puerto=[15,4,16,5,18,19,21,22,23,32]
leds=[]
for i in puerto:
    leds.append (pin(i,pin.OUT))
def derecha():
    contador=0
    inicio=0
    fin=4;
    for a in range(6):
        for i in leds[inicio:fin]:
            i.value(not i.value())
        if(contador==0):
            pausa(5)
        elif(contador==2):
            pausa(1.5)
        elif(contador==4):
            pausa(10)
        contador=contador+1
        if(contador==2):
            inicio=4
            fin=7
        elif(contador==4):
            inicio=7
            fin=10
def izquierda():
    contador=0
    inicio=7
    fin=10;
    for a in range(6):
        for i in reversed(leds[inicio:fin]):
            i.value(not i.value())
        if(contador==2):
            pausa(1.5)
        contador=contador+1
        if(contador==2):
            inicio=4
            fin=7
        elif(contador==4):
            inicio=0
            fin=4  
while True:
    derecha()
    izquierda()    