# rocket-shmocket

#### A bot trained to play Rocket League®.

This started out as a passion project when I realized I could probably never get much past the [plat-3/diamond-1](https://rocketleague.fandom.com/wiki/Competitive) skill level. So I decided to build a bot that was equally as bad.

##### Trained to play, not play well.

This is still a work in progress, but here's what we have so far:

1. An untrained [CNN-LSTM](https://machinelearningmastery.com/cnn-long-short-term-memory-networks/) model
2. A module that uses threads to record video and key presses while playing
3. A module that can press and release keys virtually

##### When you put it all together..

The end goal is to train the CNN-LSTM model using a moving window _(5 seconds??)_ of video frames as input to predict a set of keys-pressed as output.

---

### TODO

- ~~Cut down requirements.txt **IT'S SO LONG**~~not right now
- ~~Figure out how to kill the recording threads gracefully~~
- Play some games!
- Create training/validation/test datasets using video frames as input and key-press-sets as output
- Speed up model prediction?
