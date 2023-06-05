FROM osrf/ros:noetic-desktop-full

SHELL ["/bin/bash", "-c"]

ENV DISPLAY=:0
ENV QT_X11_NO_MITSHM=1

# Install catkin tools
RUN apt-get update && \
    apt-get install python3-catkin-tools -y

RUN source /opt/ros/noetic/setup.bash

WORKDIR /root/catkin_ws/

CMD ["bash"]
