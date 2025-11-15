FROM ubuntu:16.10

RUN printf "deb http://old-releases.ubuntu.com/ubuntu/ yakkety main universe multiverse restricted\n\
deb http://old-releases.ubuntu.com/ubuntu/ yakkety-updates main universe multiverse restricted\n\
deb http://old-releases.ubuntu.com/ubuntu/ yakkety-backports main universe multiverse restricted\n" > /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y openssh-client && \
    apt-get clean