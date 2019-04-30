# tinyvr

sudo apt install -y libjpeg8-dev imagemagick libv4l-dev cmake
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental
make
sudo make install
(sleep 60 ; sudo -u pi mjpg_streamer -o "output_http.so -w /usr/local/www" -i input_raspicam.so) &
