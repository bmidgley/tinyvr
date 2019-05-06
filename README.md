# tinyvr

## Pi needs to stream video

### Install video streaming on the pi:

make

sudo mkdir -p /usr/local/www

cp index.html position.cgi /usr/local/www

pip3 install pigpiod

sudo apt install -y libjpeg8-dev imagemagick libv4l-dev cmake

git clone https://github.com/bmidgley/mjpg-streamer.git

cd mjpg-streamer/mjpg-streamer-experimental

make

sudo make install

### add to the end of /etc/rc.local:

(sleep 60 ; sudo -u pi mjpg_streamer -o "output_http.so -w /usr/local/www" -i input_raspicam.so 2>&1 | /home/pi/tinyvr/driver.py) &

### to view from a phone, open in the browser:

http://raspberrypi.local:8080/?action=stream

### to view from a phone in a VR headset (google cardboard), open in the browser:

http://raspberrypi.local:8080/

