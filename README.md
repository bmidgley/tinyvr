# tinyvr

## Pi needs to stream video

### Install video streaming on the pi:

sudo mkdir -p /usr/local/www

cp index.html position.cgi servo.py /usr/local/www

pip3 install pigpiod

sudo apt install -y libjpeg8-dev imagemagick libv4l-dev cmake

git clone https://github.com/jacksonliam/mjpg-streamer.git

cd mjpg-streamer/mjpg-streamer-experimental

make

sudo make install

### add to the end of /etc/rc.local:

(sleep 60 ; sudo -u pi mjpg_streamer -o "output_http.so -w /usr/local/www" -i input_raspicam.so) &

### to view from a phone, open in the browser:

http://raspberrypi.local:8080/?action=stream

### to view from a phone in a VR headset (google cardboard), open in the browser:

http://raspberrypi.local:8080/

## Microbit needs to function as the remote and the drive

### Install microbit in ring:bit car (for another car, P1 & P2 may need to be changed to P0 & P1)

load rc-car.js into makecode.microbit.org and upload it onto the board

### Use another microbit as the controller

load rc-remote.js into makecode.microbit.org and upload it onto the board
