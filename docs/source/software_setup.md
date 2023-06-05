# Raspberry set up

## Install OS
This project is using Ubuntu 2020 as the base OS. Use the official ubuntu guide and follow step by step installation process. [^os-install]
 > __Note:__ Ubuntu Desktop 2020 is not available in the rpi-imager so Ubuntu Server 2020 is the one used. And the following command is needed to download the necessary package to configure the desktop version.
 > ```
 > sudo apt update
 > sudo apt install ubuntu-desktop
 > ```

## Set up ROS
Follow the ROS installation guide [^ros-install] to install __ROS noetic__.


## Install pigpio lib
Install the pigpio library with the following commands [^pigpio-install]

```bash
apt install unzip
wget https://github.com/joan2937/pigpio/archive/master.zip
unzip master.zip
cd pigpio-master
make
sudo make install
```

## Build the ROS package


## References

[^os-install]:[How to install Ubuntu Desktop on Raspberry Pi](https://ubuntu.com/tutorials/how-to-install-ubuntu-desktop-on-raspberry-pi-4#1-overview)

[^ros-install]:[ROS install](http://wiki.ros.org/noetic/Installation/Ubuntu)

[^pigpio-install]:[pigpio installation guide](https://abyz.me.uk/rpi/pigpio/download.html)

