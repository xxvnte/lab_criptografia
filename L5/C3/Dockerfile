FROM ubuntu:20.10

RUN printf "deb http://old-releases.ubuntu.com/ubuntu/ groovy main universe multiverse restricted\n\
deb http://old-releases.ubuntu.com/ubuntu/ groovy-updates main universe multiverse restricted\n\
deb http://old-releases.ubuntu.com/ubuntu/ groovy-backports main universe multiverse restricted\n" > /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y openssh-client && \
    apt-get clean

CMD ["tail", "-f", "/dev/null"]