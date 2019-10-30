import time
import cv2
import mss
import numpy as np
import threading
from pynput.keyboard import Key, Listener


def pauseBeforeStart(secondsToHold):
    for i in range(secondsToHold, 0, -1):
        print("Starting in {0}..".format(i), end="\r")
        time.sleep(1)
    print("                     ", end="\r")
    return None


def getTimeString():
    t = time.time()
    return "{0}{1}".format(
        time.strftime("%T", time.gmtime(t)),
        str(t)[str(t).index(".") : str(t).index(".") + 4],
    )


class Watcher(threading.Thread):
    def __init__(self, target_fps, monitor, filePath):
        threading.Thread.__init__(self)
        self.target_fps = target_fps
        self.monitor = monitor
        self.filePath = filePath
        self.shouldStop = False
        return None

    def run(self):
        vw = cv2.VideoWriter(
            self.filePath,
            cv2.VideoWriter_fourcc(*"mp4v"),
            self.target_fps,
            (self.monitor["width"], self.monitor["height"]),
        )
        with mss.mss() as sct:
            while True:
                img = np.array(sct.grab(self.monitor))
                frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                vw.write(frame)
                if self.shouldStop:
                    print("Stopped watcher.")
                    break
        return None


if __name__ == "__main__":

    # Set the folder and file name for recordings
    capturePath = "captures/"
    fileName = getTimeString()

    # Set the values for the watcher
    target_fps = 15
    monitor = {"top": 30, "left": 1925, "width": 1280, "height": 720}
    videoFilePath = "{0}{1}.mp4".format(capturePath, fileName)

    # Create the watcher
    watcher = Watcher(target_fps, monitor, videoFilePath)

    # Set the values and make the functions for the listener
    keyFilePath = "{0}{1}.key".format(capturePath, fileName)
    keyFile = open(keyFilePath, "w")

    def on_press(key):
        keyFile.write("{0} | pressed  | {1} \n".format(getTimeString(), key))

    def on_release(key):
        keyFile.write("{0} | released | {1} \n".format(getTimeString(), key))
        if key == Key.esc:
            # Stop listener
            watcher.shouldStop = True
            print("Stopped listener.")
            return False

    # Create the listener
    listener = Listener(on_press=on_press, on_release=on_release)

    # Pause for a moment to get back to the game
    pauseBeforeStart(5)

    # Start the threads
    watcher.start()
    print("Started watcher.")
    listener.start()
    print("Started listener.")

    # Wait for them
    listener.join()
    watcher.join()

    # Close the file
    keyFile.close()

