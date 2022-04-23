FROM ubuntu:20.04

RUN apt-get update -y
RUN apt-get install -y build-essential socat libseccomp-dev python3 python3-pip
RUN pip3 install pytimedinput

ARG USER
ENV USER monkey

COPY ./start.sh /start.sh
COPY ./run.py /run.py

RUN useradd -m monkey

RUN chmod 755 /start.sh

EXPOSE 9000

CMD ["/start.sh"]
