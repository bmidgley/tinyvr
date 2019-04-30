# tinyvr

## Pi needs to stream video

### Install video streaming on the pi:

sudo apt install -y libjpeg8-dev imagemagick libv4l-dev cmake

git clone https://github.com/jacksonliam/mjpg-streamer.git

cd mjpg-streamer/mjpg-streamer-experimental

make

sudo make install

### add to the end of /etc/rc.local:

(sleep 60 ; sudo -u pi mjpg_streamer -o "output_http.so -w /usr/local/www" -i input_raspicam.so) &

### view from a phone; open:

http://raspberrypi.local:8080/?action=stream

## Microbit needs to function as the remote and the drive

### Install microbit in ring:bit car (for another car, P1 & P2 may need to be changed to P0 & P1)

load rc-car.js into makecode.microbit.org and upload it onto the board

### Use another microbit as the controller

load rc-remote.js into makecode.microbit.org and upload it onto the board
