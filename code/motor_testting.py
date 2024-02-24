import numpy as np
from src import motor as motor_module
import time

if __name__ == '__main__':

    motor1 = motor_module.Motor({
        "pins": {
            "speed": 13,
            "control1": 5,
            "control2": 6
        }
    })

    motor2 = motor_module.Motor({
        "pins": {
            "speed": 12,
            "control1": 7,
            "control2": 8
        }
    })

    # speeds are 0 to 1
    speeds = list(np.linspace(0, 1, 11)) + list(np.linspace(0.9, 0, 10))

    dt = 0.25
    motor1.stop()
    motor2.stop()
    time.sleep(dt)


    for _ in range(2):
        # Forward straight
        motor1.forward(0.5)
        motor2.forward(0.5)
        time.sleep(2)

        # Right turn
        motor1.forward(0.5)
        motor2.backward(0.5)
        time.sleep(1)

        # Forward straight
        motor1.forward(0.5)
        motor2.forward(0.5)
        time.sleep(2)

        # Left turn
        motor1.backward(0.5)
        motor2.forward(0.5)
        time.sleep(1)

    

    motor1.stop()
    motor2.stop()
