FROM ros:noetic

SHELL ["/bin/bash", "-c"]

ENV DISPLAY=:0
ENV QT_X11_NO_MITSHM=1

# Install catkin tools
RUN apt-get update && \
    apt-get install python3-catkin-tools -y

# Install ROS dependencies
RUN apt-get install -y ros-noetic-rviz \
        ros-noetic-xacro \
        ros-noetic-robot-state-publisher \
        ros-noetic-joint-state-publisher-gui

RUN source /opt/ros/noetic/setup.bash

# Set up keys
apt install unzip
wget https://github.com/joan2937/pigpio/archive/master.zip
unzip master.zip
cd pigpio-master
make
sudo make install
#RUN apt-get install -y wget  
#RUN wget https://archive.raspbian.org/raspbian.public.key -O - | sudo apt-key add -


# Set up sources.list to include 
#RUN touch /etc/apt/sources.list.d/raspi.list 
#RUN echo "deb http://archive.raspbian.org/raspbian buster main contrib non-free">/etc/apt/sources.list.d/raspi.list \
#    apt-get update
# sudo apt-get install pigpio python-pigpio python3-pigpio
#RUN echo "deb http://archive.raspberrypi.org/debian/ buster main">/etc/apt/sources.list.d/raspi.list \

#RUN apt install python-pigpio  
#    systemctl start pigpiod    # start the pigpiod daemon \
#    systemctl enable pigpiod   # automatically start the daemon every time your Raspberry Pi


WORKDIR /root/catkin_ws/

CMD ["bash"]
