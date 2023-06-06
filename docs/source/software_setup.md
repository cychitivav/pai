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
Install the pigpio library with the following commands [^pigpio-install].

```bash
apt install unzip
wget https://github.com/joan2937/pigpio/archive/master.zip
unzip master.zip
cd pigpio-master
make
sudo make install
```

## Get project 
This project is configured as a ROS package. Clone the repo inside your workspace

```
cd ~/catkin_ws/src
git clone --recurse-submodules  https://github.com/cychitivav/pai
``` 

## Install driver library

```
cd ~/catkin_ws/src/pai/lib/max14870-driver
sudo python3 setup.py install
```

## Build the ROS package

```
cd ~/catkin_ws
catkin build
```
## Run robot

```
roslaunch pai run_robot.launch
```

```
rostopic pub  -r 0.5 /front_right_wheel_ctrl/command std_msgs/Float64 "64.0"
```


```
rostopic pub -r 0.5 /cmd_vel geometry_msgs/Twist "linear:
  x: 1.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.1"
```

For further configuration check out the Miscellaneous section.

<details>
  <summary><h2>Miscellaneous configuration </h2></summary>
  <p>ssh remote.</p>
  <p>development environment (install vscode and list of vscode extensions).</p>
  <p>add raspbian apt archive.</p>
  <p>configure vnc server.</p>
</details> 

## References

[^os-install]:[How to install Ubuntu Desktop on Raspberry Pi](https://ubuntu.com/tutorials/how-to-install-ubuntu-desktop-on-raspberry-pi-4#1-overview)

[^ros-install]:[ROS install](http://wiki.ros.org/noetic/Installation/Ubuntu)

[^pigpio-install]:[pigpio installation guide](https://abyz.me.uk/rpi/pigpio/download.html)

[^vnc-server-install]:[install and configure vnc on ubuntu 20-04](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-20-04)