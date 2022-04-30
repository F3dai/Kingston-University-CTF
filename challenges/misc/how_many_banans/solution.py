from pwn import *

HOST = "10.154.0.4"
PORT = 42696
conn = remote(HOST, PORT)


# Ignore initial text
conn.recvline().decode()

while True:

    res = conn.recvline().decode().strip()
    print("response: " + res)
    conn.sendline(str(len(res)).encode())
    res = conn.recvline().decode().strip()
