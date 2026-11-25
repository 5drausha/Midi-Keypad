import time
import microcontroller
import pwmio
import rotaryio
import touchio
import digitalio

t1 = touchio.TouchIn(microcontroller.pin.GPIO1)
t2 = touchio.TouchIn(microcontroller.pin.GPIO2)
t3 = touchio.TouchIn(microcontroller.pin.GPIO3)
t4 = touchio.TouchIn(microcontroller.pin.GPIO4)
t5 = touchio.TouchIn(microcontroller.pin.GPIO5)
t6 = touchio.TouchIn(microcontroller.pin.GPIO6)
t7 = touchio.TouchIn(microcontroller.pin.GPIO7)
t8 = touchio.TouchIn(microcontroller.pin.GPIO8)
t9 = touchio.TouchIn(microcontroller.pin.GPIO9)
t10 = touchio.TouchIn(microcontroller.pin.GPIO10)

bz = pwmio.PWMOut(microcontroller.pin.GPIO11, duty_cycle=0, frequency=440, variable_frequency=True)

enc = rotaryio.IncrementalEncoder(microcontroller.pin.GPIO12, microcontroller.pin.GPIO13)
last_enc = 0

b1 = digitalio.DigitalInOut(microcontroller.pin.GPIO44)
b1.direction = digitalio.Direction.INPUT
b1.pull = digitalio.Pull.UP

b2 = digitalio.DigitalInOut(microcontroller.pin.GPIO43)
b2.direction = digitalio.Direction.INPUT
b2.pull = digitalio.Pull.UP

oct_mult = 1.0
vol = 8000

while True:
    if b1.value == False:
        oct_mult = oct_mult / 2.0
        time.sleep(0.25)
    if b2.value == False:
        oct_mult = oct_mult * 2.0
        time.sleep(0.25)

    if enc.position > last_enc:
        vol = vol + 2000
        if vol > 32768:
            vol = 32768
        last_enc = enc.position
    if enc.position < last_enc:
        vol = vol - 2000
        if vol < 0:
            vol = 0
        last_enc = enc.position

    if t1.value == True:
        bz.frequency = int(262 * oct_mult)
        bz.duty_cycle = vol
    elif t2.value == True:
        bz.frequency = int(294 * oct_mult)
        bz.duty_cycle = vol
    elif t3.value == True:
        bz.frequency = int(330 * oct_mult)
        bz.duty_cycle = vol
    elif t4.value == True:
        bz.frequency = int(349 * oct_mult)
        bz.duty_cycle = vol
    elif t5.value == True:
        bz.frequency = int(392 * oct_mult)
        bz.duty_cycle = vol
    elif t6.value == True:
        bz.frequency = int(440 * oct_mult)
        bz.duty_cycle = vol
    elif t7.value == True:
        bz.frequency = int(494 * oct_mult)
        bz.duty_cycle = vol
    elif t8.value == True:
        bz.frequency = int(523 * oct_mult)
        bz.duty_cycle = vol
    elif t9.value == True:
        bz.frequency = int(587 * oct_mult)
        bz.duty_cycle = vol
    elif t10.value == True:
        bz.frequency = int(659 * oct_mult)
        bz.duty_cycle = vol
    else:
        bz.duty_cycle = 0

    time.sleep(0.01)