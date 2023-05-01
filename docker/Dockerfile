FROM ros:humble

RUN apt update && apt upgrade -y && \
    apt install python3-pip -y 

RUN pip3 install sphinx

WORKDIR /root/ros2_ws/src

CMD ["bash"]
