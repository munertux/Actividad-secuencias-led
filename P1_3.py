from machine import Pin
import utime
led1=Pin(15,Pin. OUT)
led2=Pin(4,Pin. OUT)
led3=Pin(16,Pin. OUT)
led4=Pin(5,Pin. OUT)
led5=Pin(18,Pin. OUT)
led6=Pin(19,Pin. OUT)
led7=Pin(21,Pin. OUT)
led8=Pin(22,Pin. OUT)
led9=Pin(23,Pin. OUT)
led10=Pin(32,Pin. OUT)
semaforo=[led1,led2,led3,led4,led5,led6,led7,led8,led9,led10]
def derecha():
    contador1=0
    for a in semaforo:
        a.value(1)   
        if(contador1==3):
            utime.sleep(5)
        elif(contador1==6 ):
            utime.sleep(1.5)
        elif(contador1==9):
            utime.sleep(10)
        if (a == led4 or a==led7 or a==led10):
            for i in semaforo[0:10]:
                i.value(0)
        contador1=contador1+1
def izquierda():
    contador1=0
    for a in reversed(semaforo):
        a.value(1)   
        if(contador1==5 ):
            utime.sleep(1.5)
        if (a == led8 or a==led5 or a==led1):
            for i in reversed(semaforo[0:10]):
                i.value(0)
        contador1=contador1+1
while True:
    derecha() 
    izquierda()