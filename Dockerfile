FROM osrf/ros:noetic-desktop-full

SHELL ["/bin/bash", "-c"]

ENV DISPLAY=:0
ENV QT_X11_NO_MITSHM=1

# Install catkin tools
RUN apt-get update && \
    apt-get install python3-catkin-tools -y

RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

# Install pigpio
RUN apt-get install -y wget unzip && \
    wget https://github.com/joan2937/pigpio/archive/master.zip && \
    unzip master.zip && \
    cd pigpio-master && \
    make && \
    make install && \
    cd .. && \
    rm -rf pigpio-master && \
    rm master.zip

WORKDIR /root/catkin_ws/

CMD ["bash"]
