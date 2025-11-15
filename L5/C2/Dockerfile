FROM ubuntu:18.10

RUN printf "deb http://old-releases.ubuntu.com/ubuntu/ cosmic main universe multiverse restricted\n\
deb http://old-releases.ubuntu.com/ubuntu/ cosmic-updates main universe multiverse restricted\n\
deb http://old-releases.ubuntu.com/ubuntu/ cosmic-backports main universe multiverse restricted\n" > /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y openssh-client && \
    apt-get clean

CMD ["tail", "-f", "/dev/null"]