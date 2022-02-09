# Monkey Sit

```

```

Steganography (I know, not realistic but fun for new starters).

A file is hidden using steghide.

```
steghide info me.jpg
```

Flag is base64 encoded

```
cat flag.txt | base64 -d
```

## Build and deploy

```
cd challenge
make -C challenge && kctf chal start
```

## Healthcheck

```
make -C healthcheck
```
