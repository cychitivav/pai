FROM ros:humble

WORKDIR /root/ros2_ws

RUN apt update && apt upgrade -y && \
    apt install python3-pip -y 

CMD ["bash"]
