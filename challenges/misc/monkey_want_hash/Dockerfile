FROM ubuntu:16.04

RUN apt-get update
RUN apt-get update && apt-get install -y build-essential socat libseccomp-dev python3
RUN python -m pip install pytimedinput hashlib

ARG USER
ENV USER $USER

COPY ./start.sh /start.sh
COPY ./run.py /run.py

RUN useradd -m $USER

RUN chmod 755 /start.sh

EXPOSE 9000

CMD ["/start.sh"]