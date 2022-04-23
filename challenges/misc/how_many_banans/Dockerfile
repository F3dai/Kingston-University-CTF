FROM ubuntu:20.04

RUN apt-get update && apt-get install -y build-essential socat libseccomp-dev python3

ARG USER
ENV USER monkey

COPY ./start.sh /start.sh
COPY ./run.py /run.py

RUN useradd -m $USER

RUN chmod 755 /start.sh

EXPOSE 9000

CMD ["/start.sh"]
