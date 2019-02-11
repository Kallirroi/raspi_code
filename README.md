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

### dat

`npm install -g dat` or `npm install -g dat@v13.10.0`
`npm install dat-node`

### dat troubleshooting
`rm -rf .dat/` if it complains about another `hypercore` instance.
copy recordings to folder within `dat_code` if it complains about not being owner of archive.
