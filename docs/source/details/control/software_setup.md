# Raspberry set up

## Install OS
This project is using Ubuntu 20.04 as the base OS. Use the official ubuntu guide and follow step by step installation process. [^os-install]

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
sudo rm -rf master.zip pigpio-master
```

## Get project 
This project is configured as a ROS package. Clone the repo inside your workspace

```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone https://github.com/cychitivav/pai
```

## Build the ROS package

```bash
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

## Slow boot time
At start up the `systemd-networkd-wait-online.service` waits for a network to be connected. Which makes the the start up time really long if no network is connected. You change the configuration of the service in order to reduce the wait time. Find the line  that starts with `ExecStart=[PATH]`inside the  `systemd-networkd-wait-online.service` and add the  parameter `--timeout=10`

```
sudo systemctl disable NetworkManager-wait-online.service
sudo nano  systemd-networkd-wait-online.service
#  ExecStart=/lib/systemd/systemd-networkd-wait-online --timeout=10
```

## Autostart pigpio deamon at boot
If `pigpio` is installed from the source code, the deamon needs to be started manually, due to the fact that the installation process does not create a service. To start the deamon at boot, create a service configuration file in the following path `/etc/systemd/system/pigpiod.service.d/public.conf` and add the following lines.

```conf
[Service]
ExecStart=
ExecStart=/usr/local/bin/pigpiod
```

Then, create the service file `/lib/systemd/system/pigpiod.service` and add the following lines.

```conf
[Unit]
Description=Daemon required to control GPIO pins via pigpio
[Service]
ExecStart=/usr/local/bin/pigpiod
ExecStop=/bin/systemctl kill -s SIGKILL pigpiod
Type=forking
[Install]
WantedBy=multi-user.target
```

And finally, enable and start the service.

```bash
sudo systemctl deamon-reload
sudo systemctl enable pigpiod
sudo systemctl start pigpiod
```


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