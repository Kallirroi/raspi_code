# raspi_code
Rapsberry Pi code for my thesis

### raspi stuff
- download and burn raspian image (I am using this 2018-06-27-raspbian-stretch)
- set password, country, wifi network (MIT)
- enable SSH

### install rmate
to load code on your client via SSH 

`sudo wget -O /usr/local/bin/rmate https://raw.githubusercontent.com/aurora/rmate/master/rmate`

`sudo chmod a+x /usr/local/bin/rmate`

`sudo nano ~/.bashrc` for the `ll` alias

### install pyaudio
`sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev`

`pip3 install pyaudio`

` sudo nano /usr/share/alsa/alsa.conf` for modifying the ALSA file - or use `alsamixer` and F6 and then `sudo alsactl store 1`

then reboot - make sure the card is plugged into the USB.

`alsamixer -c 1` for setting microphone volume

### install Node and npm

`sudo apt-get update && sudo apt-get upgrade` to make sure system is up to date.

`wget -qO- https://deb.nodesource.com/setup_8.x | sudo bash` 

`source ~/.nvm/nvm.sh`

`nvm install 8.15.0` and `nvm use 8.15.0` to install Node and npm.

`sudo apt-get install -y nodejs` 


### install dat

`npm install -g dat` 

`npm install dat-node`

### Details about how they share files using dat
It is not trivial, but I will try to do my best to explain. Essentially you need the same Raspberry to be running `send.js` and `receive.js` at the same time, in order to both send and receive files. However, since they both instantiate a `.dat` folder in the directories in which they are run, they can't be run on the same directory. To get over that, I separated the incoming and outgoing file streams into different folders. Each object sends their `/raspi_code/recordings/` files, and receives files in the `/raspi_code/dat_code/recordings/` directory. A cron job then moves them to `/raspi_code/recordings/` so they can be fed to the playback.

1. In `/raspi_code/dat_code/`, running `node send.js` provides the dat URL for the machine.

2. Copy that to the recipient directory's receive.js file. The paths should all be relative e.g. `./test` rather than the absolute path.

3.`node receive.js`
in the "recipient" directory, after having entered the dat URL. Make sure there is no existing `.dat/` directory anywhere there, there will be an issue with `hypercore`.

### dat troubleshooting
`rm -rf .dat/` if it complains about another `hypercore` instance.

### twitter_object
Go in the `twitter` directory: 

`pip3 install tweepy`

`pip3 install SpeechRecognition`

### Process management (PM2)
For the purposes of testing, you can run `python3 main.py` to start the playback + listening to button press for recording. However we want some sort of process manager to make sure that the objects are running this correctly in the background. I am using PM2 in this case.

`npm install pm2@latest -g`

Set path: 

`sudo env PATH=$PATH:/usr/local/bin pm2 startup systemd -u pi --hp /home/pi`

Start the `main.py` script using the Python interpreter for `pm2`:

`pm2 start main.py --interpreter=python3 --log-date-format 'DD-MM HH:mm:ss.SSS' `

`pm2 save`

If you need to restart (which you will need to): 

`pm2 flush && pm2 restart main --update-env  --log-date-format 'DD-MM HH:mm:ss.SSS'` for restarting the main process 

Since the Dat scripts are Node-based, pm2 is perfect for them - you can just add them to the `pm2` stack. Go to the `dat_code` directory: 

`pm2 start send.js --name dat-send` for starting the "send" process

`pm2 start receive.js --name dat-receive` for starting the "receive" process.

Any questions? Email me!
