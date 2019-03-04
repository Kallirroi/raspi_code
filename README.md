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

` sudo nano /usr/share/alsa/alsa.conf` for modifying the ALSA file 

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

I need to make sure that `send.js` and `receive.js` are always running on the background. I have made a crontab for `update_recordings.sh` (do `crontab- e` and then `0 * * * *  /home/pi/raspi_code/dat_code/update_recordings.sh` to set it).

### systemd

For creating `systemd` services:

`sudo nano /etc/systemd/system/script_name.service` to create a service. For sending files using dat:

```
[Unit]
Description=send
After=network.target

[Service]
ExecStart=/home/pi/.nvm/versions/node/v8.15.0/bin/node send.js
WorkingDirectory=/home/pi/raspi_code/dat_code/
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

and for receiving: 

```
[Unit]
Description=send
After=network.target

[Service]
ExecStart=/home/pi/.nvm/versions/node/v8.15.0/bin/node receive.js
WorkingDirectory=/home/pi/raspi_code/dat_code/
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

`sudo systemctl start scrpt_name.service` and if it works well, 

`sudo systemctl enable script_name.service`

`sudo systemctl daemon-reload` if needed to reload and

`sudo systemctl status script_name.service` to check errors.

It should create this `Created symlink /etc/systemd/system/multi-user.target.wants/run_send.service → /etc/systemd/system/run_send.service.` if all goes well. 
