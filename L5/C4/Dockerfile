FROM ubuntu:22.10

RUN printf "deb http://old-releases.ubuntu.com/ubuntu/ kinetic main universe multiverse restricted\n\
deb http://old-releases.ubuntu.com/ubuntu/ kinetic-updates main universe multiverse restricted\n\
deb http://old-releases.ubuntu.com/ubuntu/ kinetic-backports main universe multiverse restricted\n" > /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y openssh-client openssh-server && \
    apt-get clean

RUN useradd -m -s /bin/bash test
RUN echo "test:test" | chpasswd

RUN mkdir /var/run/sshd
EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]