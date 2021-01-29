
# Existing docker image as base
FROM ros:noetic


RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
RUN mkdir -p /home/catkin_ws/src
WORKDIR /home/catkin_ws/src

RUN /bin/bash -c '. /opt/ros/noetic/setup.bash; catkin_init_workspace /home/catkin_ws/src'

WORKDIR /home/catkin_ws
RUN /bin/bash -c '. /opt/ros/noetic/setup.bash; cd /home/catkin_ws; catkin_make'
RUN echo "source /home/catkin_ws/devel/setup.bash" >> ~/.bashrc

