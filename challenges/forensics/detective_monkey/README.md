# Monkey Selfie

```
Someone has downloaded sensitive files from a website.
Detective monkey has been asked to investigate.
```

A file is available - it is a pcap file with some web traffic.

Investigate the web traffic and find any downloaded files.

https://www.techwalla.com/articles/how-to-get-images-from-wireshark

## Build and deploy

```
cd challenge
make -C challenge && kctf chal start
```

## Healthcheck

```
make -C healthcheck
