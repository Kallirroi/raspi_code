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

` sudo nano /usr/share/alsa/alsa.conf` for modifying the ALSA file - or use `alsamixer` and F6 and then `sudo alsactl store 1`

then reboot - make sure the card is plugged into the USB.

`alsamixer -c 1` for setting microphone volume

### Node and npm

`sudo apt-get update && sudo apt-get upgrade` to make sure system is up to date.

`wget -qO- https://deb.nodesource.com/setup_8.x | sudo bash` 

`source ~/.nvm/nvm.sh`

`nvm install 8.15.0` and `nvm use 8.15.0` to install Node and npm.

`sudo apt-get install -y nodejs` 


### dat

`npm install -g dat` 

`npm install dat-node`

### dat sharing files
1. `node send.js`
to get the dat URL.

2. Copy that to the recipient directory's receive.js file. The paths should all be relative e.g. `./test` rather than the absolute path.

3.`node receive.js`
in the "recipient" directory, after having entered the dat URL. Make sure there is no existing `.dat/` directory anywhere there, there will be an issue with `hypercore`.

Each object sends their `/raspi_code/recordings/` files, and receives files in the `/raspi_code/dat_code/recordings/` directory. A cron job then moves them to `/raspi_code/recordings/` so they can be fed to the playback.


### dat troubleshooting
`rm -rf .dat/` if it complains about another `hypercore` instance.


After all this is done, running `python3 main.py` should start the playback + listening to button press for recording.

### twitter_object
`pip3 install tweepy`

`pip3 install SpeechRecognition`

`python3 main.py`

### cron

I need to make sure that `send.js` and `receive.js` are always running on the background. I have made a crontab for `update_recordings.sh` (do `crontab- e` and then `*/30 * * * *  /home/pi/raspi_code/dat_code/update_recordings.sh` to set it).

### pm2

`npm install pm2@latest -g`

`pm2 start main.py --interpreter=python3 --log-date-format 'DD-MM HH:mm:ss.SSS' --name app ` 

`sudo env PATH=$PATH:/usr/local/bin pm2 startup systemd -u pi --hp /home/pi`

`pm2 save`

`pm2 flush && pm2 restart main --update-env  --log-date-format 'DD-MM HH:mm:ss.SSS'` for restarting the main process 

for dat, in the `dat_code` directory: 

`pm2 start send.js --name dat-send`

`pm2 start receive.js --name dat-receive` 
