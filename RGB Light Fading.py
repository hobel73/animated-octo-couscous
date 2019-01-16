import pulseio
import board
import time


rled = pulseio.PWMOut(board.D4, frequency=10000, duty_cycle=0)
gled = pulseio.PWMOut(board.D0, frequency=10000, duty_cycle=0)
bled = pulseio.PWMOut(board.D2, frequency=10000, duty_cycle=0)

slp = .1



while True:
    for i in range(100):

            # PWM LED up and down
        if i < 50:
            rled.duty_cycle = int(i * 2 * 65535 / 100)  # Up
            # gled.duty_cycle = int(i * 2 * 65535 / 100)  # Up
            # bled.duty_cycle = int(i * 2 * 65535 / 100)  # Up
        else:
            rled.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
            # gled.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
            # bled.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
        time.sleep(slp)
        print("Red Finished")


    for i in range(100):

            # PWM LED up and down
        if i < 50:
            # rled.duty_cycle = int(i * 2 * 65535 / 100)  # Up
            # gled.duty_cycle = int(i * 2 * 65535 / 100)  # Up
            bled.duty_cycle = int(i * 2 * 65535 / 100)  # Up
        else:
            # rled.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
            # gled.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
            bled.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
        time.sleep(slp)
        print("Blue Finished")


    for i in range(100):

            # PWM LED up and down
        if i < 50:
            rled.duty_cycle = int(i * 2 * 65535 / 100)  # Up
            # gled.duty_cycle = int(i * 2 * 65535 / 100)  # Up
            bled.duty_cycle = int(i * 2 * 65535 / 100)  # Up
        else:
            rled.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
            # gled.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
            bled.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
        time.sleep(slp)
        print("Purple Finished")