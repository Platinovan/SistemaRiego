# Codigo elaborado por: Cuevas Martinez Jose Luis
#Para el proyecto de Desarrollo de habilidades del pensamiento
from machine import Pin, I2C
from PicoDHT22 import PicoDHT22
from ssd1306 import SSD1306_I2C
import utime as time
from time import sleep
import _thread

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)
dht_sensor=PicoDHT22(Pin(28),dht11=True)

print("I2C Address      : "+hex(i2c.scan()[0]).upper())
print("I2C Configuration: "+str(i2c))
oled = SSD1306_I2C(128, 32, i2c)

def rele():
    relevador = machine.Pin(5, machine.Pin.OUT)
    touch = machine.Pin(4, machine.Pin.IN)
    while True:
        if touch.value() == 1:
            relevador.value(1)
        else:
            relevador.value(0)
            
_thread.start_new_thread(rele,())
    
while True:
    T, H = dht_sensor.read()
    oled.fill(0)
    
    if T is None:
        print("Error en el sensor!")
        oled.text("Sensor Error", 0, 0);
        oled.show()
    else:
        print("{}'C  {}%".format(T,H))
        #Imprimir temperatura
        oled.text("Temp: ", 0, 0)
        oled.text(str(T), 50, 0)
        oled.text("^C",  70, 0)
        #Imprimir Humedad
        oled.text("Hum: ", 0, 20)
        oled.text(str(H), 40, 20)
        oled.text("%", 60, 20)
        oled.show()
        sleep(1)