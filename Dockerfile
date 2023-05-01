FROM ros:humble

# Install sphinx
RUN apt update && apt upgrade -y && \
    apt install python3-pip -y 

# Install latex packages to build pdfs
RUN apt install -y texlive-latex-recommended && \
    apt install -y texlive-latex-extra && \
    apt install -y texlive-fonts-recommended && \
    apt install -y latexmk && \
    apt install -y tex-gyre

RUN pip3 install sphinx

COPY docs/requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

WORKDIR /root/ros2_ws/src

CMD ["bash"]
