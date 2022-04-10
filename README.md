# nature-audio-ai
## Audio classification and event detection of natural audio recordings.


Read about SED (Sound Event Detection) here: https://www.kaggle.com/code/hidehisaarai1213/introduction-to-sound-event-detection/notebook - this was my starting point.

The series of notebooks with PANN-SED-1A all relate to the latest classification model which uses a modified version of the SED attention network here  https://github.com/qiuqiangkong/audioset_tagging_cnn/

There is a notebook for training, prediction, and extracting features from the final linear layer. Training is based on the  I am working on a clustering notebook.

Training is based on data from https://www.kaggle.com/competitions/birdclef-2021 along with other data.  Format of data is similar to this contest data.

## Other repos

* For Hardware used for recording - see: https://hackaday.io/project/179489-high-performance-audio-adc-for-machine-learning
* For Firmware for continuous recording -see: https://github.com/filipmu/audio-recording-firmware-raspi-tlv320adc6140
* For a web app for browsing predictions - see: https://github.com/filipmu/animal-sound-detection-app
