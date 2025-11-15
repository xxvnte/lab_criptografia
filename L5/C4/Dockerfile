FROM ubuntu:22.10

RUN sed -i 's/archive.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list
RUN apt-get update && \
    apt-get install -y openssh-client openssh-server && \
    apt-get clean

RUN useradd -m -s /bin/bash test
RUN echo "test:test" | chpasswd

RUN mkdir /var/run/sshd
EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]