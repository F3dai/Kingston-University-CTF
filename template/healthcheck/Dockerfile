FROM gcr.io/kctf-docker/healthcheck@sha256:abe5bc78f1eed01a050bc9efccde279aef560888598c0a04547b383a1429c6d4

COPY healthcheck_loop.sh healthcheck.py healthz_webserver.py /home/user/

CMD kctf_drop_privs /home/user/healthcheck_loop.sh & /home/user/healthz_webserver.py
