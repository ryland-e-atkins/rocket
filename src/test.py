import time
import cv2
import mss
import numpy as np

MONITOR = {"top": 30, "left": 1925, "width": 1280, "height": 720}


with mss.mss() as sct:
    img = np.array(sct.grab(MONITOR))
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
