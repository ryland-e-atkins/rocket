import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "0"

import numpy as np
import time

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import TimeDistributed
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense


input_shape = (4, 720, 1280, 4)

model = Sequential()
model.add(
    TimeDistributed(Conv2D(8, (20, 20), activation="relu"), input_shape=input_shape)
)
model.add(TimeDistributed(MaxPool2D(pool_size=(2, 2))))
model.add(TimeDistributed(Flatten()))
model.add(LSTM(8))
model.add(Dense(8))

model.compile(loss="binary_crossentropy", optimizer="adam", metric=["accuracy"])

print("starting...")
sum_time = 0
for i in range(10):

    start_time = time.time()

    x = [[np.ones(input_shape)]]
    model.predict(x)
    iter_time = time.time() - start_time
    print("iteration {0}: {1}".format(i, iter_time))
    sum_time += iter_time


print("\naverage prediction time: {0}".format(sum_time / 10))

