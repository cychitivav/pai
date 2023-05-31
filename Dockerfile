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

WORKDIR /root/catkin_ws/

CMD ["bash"]
