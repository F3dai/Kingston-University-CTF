# Kingston-University-CTF

Capture the flag competition for Kingston University Cyber Security Society

This repo contains all challenges, flags and infrastructure configuration.

## Template

Find a template challenge in /template

Each challenge must have the same directory layout and configuration files to work with kCTF.

## K8S

 - A cluster is a collection of challenges
 - A challenge = K8S deployment
 - Healthcheck = container that can run test exploit. 
 - nsjail = creates new environment for every TCP connection.

From kCTF:

![kCTF infrastructure](https://google.github.io/kctf/images/introduction-k8s.png)

## Rules

Duration for the CTF will be 24 – 48 hours. Therefore, need to provide VPN for 24 or so hour access to challenges.

No teams.

All challenges must be completely authentic to avoid cheating.

We need to get sign ups to anticipate how many participants so we can configure the servers properly + give out VPN configs.

kucybersec.co.uk/ctf