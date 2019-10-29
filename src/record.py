import time
import cv2
import mss
import numpy as np
import threading
from pynput.keyboard import Key, Listener

CAP_FOLDER = "captures/"
MONITOR = {"top": 0, "left": 1920, "width": 1280, "height": 720}
TARGET_FPS = 15


def getTimeString():
    t = time.time()
    return "{0}{1}".format(
        time.strftime("%T", time.gmtime(t)),
        str(t)[str(t).index(".") : str(t).index(".") + 4],
    )


timeString = getTimeString()
videoFileName = "{0}{1}.mp4".format(CAP_FOLDER, timeString)
keyFileName = "{0}{1}.key".format(CAP_FOLDER, timeString)

keyFile = open(keyFileName, "w")


def recordVideo():
    print("Recording video..")
    vw = cv2.VideoWriter(
        videoFileName,
        cv2.VideoWriter_fourcc(*"mp4v"),
        TARGET_FPS,
        (MONITOR["width"], MONITOR["height"]),
    )
    with mss.mss() as sct:
        while True:
            img = np.array(sct.grab(MONITOR))
            frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            vw.write(frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                print("Stopped recording.")
                break
    return


def on_press(key):
    keyFile.write("{0} | pressed  | {1} \n".format(getTimeString(), key))
    print("{0} pressed".format(key))


def on_release(key):
    keyFile.write("{0} | released | {1} \n".format(getTimeString(), key))
    print("{0} released".format(key))
    if key == Key.esc:
        # Stop listener
        print("Stopped key listener.")
        return False


def recordKeys():
    print("Recording keys..")
    with Listener(on_press=on_press, on_release=on_release) as keyListener:
        keyListener.join()


if __name__ == "__main__":
    screenRecorder = threading.Thread(target=recordVideo)
    screenRecorder.start()
    recordKeys()
    screenRecorder.join()
    keyFile.close()

