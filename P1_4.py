from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau
led1=pin(15,pin. OUT)
led2=pin(4,pin. OUT)
led3=pin(16,pin. OUT)
led4=pin(5,pin. OUT)
led5=pin(18,pin. OUT)
led6=pin(19,pin. OUT)
led7=pin(21,pin. OUT)
led8=pin(22,pin. OUT)
led9=pin(23,pin. OUT)
led10=pin(32,pin. OUT)
semaforo=[led1,led2,led3,led4,led5,led6,led7,led8,led9,led10]
for a in semaforo:
    a.value(0)
def derecha():
    contador=0
    inicio=0
    fin=4;
    for a in range(6):
        for i in semaforo[inicio:fin]:
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
        for i in reversed(semaforo[inicio:fin]):
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
       