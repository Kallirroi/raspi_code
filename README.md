# raspi_code
Rapsberry Pi code for my thesis


### raspi stuff
- download and burn raspian image (I am using this 2018-06-27-raspbian-stretch)
- set password, country, wifi network (MIT)
- enable SSH

### rmate
`sudo wget -O /usr/local/bin/rmate https://raw.githubusercontent.com/aurora/rmate/master/rmate`

`sudo chmod a+x /usr/local/bin/rmate`

`sudo nano ~/.bashrc` for the `ll` alias

### pyaudio
`sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev`

`pip3 install pyaudio`

`amixer set PCM -- 100%` for setting max volume on Pi

### Node and npm

`sudo apt-get update && sudo apt-get upgrade` to make sure system is up to date.

`wget -qO- https://deb.nodesource.com/setup_8.x | sudo bash` 

`sudo apt-get install -y nodejs` 

`nvm install 8.15.0` and `nvm use 8.15.0` to install Node and npm.

### dat

`npm install -g dat` 

`npm install dat-node`

### dat sharing files
1. `node send.js`
to get the dat URL.

2. Copy that to the recipient directory's receive.js file. The paths should all be relative e.g. `./test` rather than the absolute path.

3.`node receive.js`
in the "recipient" directory, after having entered the dat URL. Make sure there is no existing `.dat/` directory anywhere there, there will be an issue with `hypercore`.


### dat troubleshooting
`rm -rf .dat/` if it complains about another `hypercore` instance.

### bot
`pip install tweepy`
`pip install SpeechRecognition`
