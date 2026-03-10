import digitalio
import board
import time

relay = digitalio.DigitalInOut(board.D13)
relay.direction = digitalio.Direction.OUTPUT

while True:
    relay.value = not relay.value
    print(f"Relay = {relay.value}")

    time.sleep(1)