"""
* Key mappings are as follows:
Drive Forward ----------------- : W
Drive Backwards                 : S
Steer Right ------------------- : D
Steer Left                      : A
Jump -------------------------- : J
Boost                           : B
Powerslide -------------------- : Left Shift
Air Steer Right                 : D
Air Steer Left ---------------- : A
Air Pitch Up                    : S
Air Pitch Down ---------------- : W
Air Roll Right                  : E
Air Roll Left ----------------- : Q
Air Roll                        : Left Shift
Focus On Ball ----------------- : Space
Rear View                      : H
Quick Chat - Info/Post Game     : 1
Quick Chat - Compliments ------ : 2
Quick Chat - Reactions          : 3
Quick Chat - Apologies -------- : 4
"""
from pynput.keyboard import Key, Controller, Listener
import random
import time


class Keytroller:
    def __init__(self, key, probPress, probRelease):
        self.pressed = False
        self.key = key
        self.probPress = probPress
        self.probRelease = probRelease


actions = {
    "DRIVE_FORWARD": Keytroller("w", 0.95, 0.10),
    "DRIVE_BACKWARD": Keytroller("s", 0.10, 0.70),
    "STEER_RIGHT": Keytroller("d", 0.50, 0.50),
    "STEER_LEFT": Keytroller("a", 0.50, 0.50),
    "JUMP": Keytroller("j", 0.30, 1.00),
    "BOOST": Keytroller("b", 0.75, 0.60),
    "POWERSLIDE": Keytroller(Key.shift_l, 0.30, 0.60),
    "FOCUS_ON_BALL": Keytroller(Key.space, 0.50, 1.00),
    "REAR_VIEW": Keytroller("h", 0.10, 0.10),
}


ctrl = Controller()


def shouldDo(prob):
    """
    Takes a probability between 1 and 0 and returns true or false
    """
    return prob > random.randint(1, 100) / 100


def pressKeys():
    """
    Presses some keys maybe
    """
    for action, actionValues in actions.items():
        if actionValues.pressed:
            if shouldDo(actionValues.probRelease):
                ctrl.release(actionValues.key)
                actions[action].pressed = False
        else:
            if shouldDo(actionValues.probPress):
                ctrl.press(actionValues.key)
                actions[action].pressed = True


def showKeys():
    """
    Prints the current values of the actions
    """
    for action, actionValues in actions.items():
        print("{0} | pressed : {1}".format(action, actionValues.pressed))


# Let's do some stuff
running = True

time.sleep(5)
while running:
    pressKeys()
    time.sleep(1.0)
