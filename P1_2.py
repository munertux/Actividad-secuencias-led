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
def semaforo(a,b,c):
  led1.value(a)
  led2.value(a)
  led3.value(a)
  led4.value(a)
  led5.value(b)
  led6.value(b)
  led7.value(b)
  led8.value(c)
  led9.value(c)
  led10.value(c)
  if (a == 1):
    pausa(5)
  elif (b == 1):
    pausa(1.5)
  elif (c==1):
    pausa(10)
while True:
    semaforo(1,0,0)
    semaforo(0,1,0)
    semaforo(0,0,1)