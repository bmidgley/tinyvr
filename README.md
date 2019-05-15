# tinyvr

## Pi needs to stream video and steer motors

### Install video streaming and controller on the pi:

cd tinyvr

make

cd

sudo apt install -y libjpeg8-dev imagemagick libv4l-dev cmake

git clone https://github.com/bmidgley/mjpg-streamer.git

cd mjpg-streamer/mjpg-streamer-experimental

make

sudo make install

### add to the end of /etc/rc.local:

pigpiod &

(sleep 60 ; sudo -u pi mjpg_streamer -o "output_http.so -w /home/pi/tinyvr/www" -i "input_raspicam.so -fps 20" 2>&1 | /home/pi/tinyvr/driver.py) &

### to view from a phone in a VR headset (google cardboard) and drive the robot, open in the chrome browser:

http://raspberrypi.local:8080/

### to view only from a browser, open in the browser:

http://raspberrypi.local:8080/?action=stream

