import machine
import network
import secrets
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect(secrets.SSID, secrets.PASSWORD)

def light_onboard_led():
    led = machine.Pin('LED', machine.Pin.OUT)
    led.on();
    
timeout = 10
while timeout > 0:
    if wlan.status() >= 3:
        light_onboard_led()
        break
    timeout -= 1
    print("Waiting for connection...")
    time.sleep(1)
    
wlan_status = wlan.status()
