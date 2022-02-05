# Banana Crypt

```
A secret message given to you by a French monkey. 
This is EXCLUSIVELY for you, OR it won't work.

key = banana
message = DhQeEggaEVABBhw+ChMbEgsJGhw=
```

Simple cryptography challenge consisting of base64 cipher text. The description of this challenge hints a French cipher and XOR. 

Base64 > XOR > Vigenere

https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)XOR(%7B'option':'UTF8','string':'banana'%7D,'Standard',false)Vigen%C3%A8re_Decode('banana')&input=RGhRZUVnZ2FFVkFCQmh3K0NoTWJFZ3NKR2h3PQ

## Build and deploy

```
cd challenge
make -C challenge && kctf chal start
```

## Healthcheck

```
make -C healthcheck
```