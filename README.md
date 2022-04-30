# Kingston-University-CTF

Capture the flag competition for Kingston University Cyber Security Society

This repo contains all challenges, flags and infrastructure configuration.

## Setup

Setup dockerd with TLS for CTFd to have access to containers - https://docs.docker.com/engine/security/protect-access/

Stop all instances of docker running and run:

```
sudo pkill docker
sudo dockerd --tlsverify --tlscacert=ca.pem --tlscert=server-cert.pem --tlskey=server-key.pem -H=0.0.0.0:2376
```

Install CTFd

Revert to 3.2.1

Clone https://github.com/offsecginger/CTFd-Docker-Challenges - edit some code in CTFd for this to work.

`head -c 64 /dev/urandom > .ctfd_secret_key `

Run CTFd in container. It's important to use -H localhost:2376 all the time so CTFd container can reach the images. 

`docker-compose -H localhost:2376 --tlsverify --tlscacert ~/cert/ca.pem --tlscert ~/cert/cert.pem --tlskey ~/cert/key.pem up`

/admin/docker_config should see all docker images.

## Rules

Duration for the CTF will be 24 – 48 hours. Therefore, need to provide VPN for 24 or so hour access to challenges.

No teams.

All challenges must be completely authentic to avoid cheating.

We need to get sign ups to anticipate how many participants so we can configure the servers properly + give out VPN configs.
