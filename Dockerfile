FROM ros:noetic

ARG ROS_DISTRO=noetic
SHELL ["/bin/bash", "-c"]

ENV DISPLAY=:0
ENV QT_X11_NO_MITSHM=1

# Install catkin tools
RUN apt update && \
    apt-get install python3-catkin-tools -y

# Install ROS dependencies
RUN apt install ros-$ROS_DISTRO-rviz -y && \
    apt install ros-$ROS_DISTRO-xacro -y && \
    apt install ros-$ROS_DISTRO-robot-state-publisher -y && \
    apt install ros-$ROS_DISTRO-joint-state-publisher-gui -y

RUN source /opt/ros/$ROS_DISTRO/setup.bash

WORKDIR /root/catkin_ws/

CMD ["bash"]
