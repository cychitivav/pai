docker build -t pai:latest docker/

docker run -it \
           --rm \
           --name pai \
           -v $PWD:/root/ros2_ws/src/pai \
           pai:latest 