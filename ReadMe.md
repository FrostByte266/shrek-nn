# shrek-nn - Detecting puns with neural networks
### This respository was created for a High School project
## State - Partially Completed (Continued in [pun_detector](https://github.com/FrostByte266/pun_detector))
## New skills learned:
* LSTM for speech pattern analysis
* Natural Language Processing
* Unit Testing
* Basic web scraping for data collection
## Skills improved upon:
* Python
* Docker
* Tensorflow / Keras
* PySimpleGui

# Pun detection with neural networks

### Overview

This uses supervised learning with neural networks in an attempt to identify a Pun

### How to use it

* Make sure docker is installed on your system

* Clone the repository
```bash
git clone https://github.com/FrostByte266/shrek-nn.git
```
* Build the image
```bash
docker build -t shrek .
```

* Run the container
```bash
chmod +x container
./container
```
or
```bash
bash container
```
* Run the driver program
```bash
python src/runner.py
```

### How it works

The program uses the TF-IDF (Term Frequency - Inverse Document) to serialize strings into data to be fed into a neural network

### Performance

Due to random initialization, network accuracy can wildly vary
