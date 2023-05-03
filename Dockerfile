FROM ros:humble

WORKDIR /root/ros2_ws

RUN apt update && apt upgrade -y && \
    apt install python3-pip -y 

## SPHINX
# Install latex packages to build pdfs
RUN apt install -y texlive-latex-recommended && \
    apt install -y texlive-latex-extra && \
    apt install -y texlive-fonts-recommended && \
    apt install -y latexmk && \
    apt install -y tex-gyre

# Install sphinx and required packages
RUN pip3 install sphinx && \
    pip3 install myst-parser && \  
    pip3 install sphinx-book-theme


ADD ./docs/requirements.txt /root/ros2_ws/src/pai/docs/requirements.txt
RUN pip3 install -r src/pai/docs/requirements.txt

CMD ["bash"]
