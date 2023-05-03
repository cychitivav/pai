docker build -t pai:latest .

docker run -it --rm -v $PWD:/root/ros2_ws/src/pai pai:latest /bin/bash -c "cd docs && make html"