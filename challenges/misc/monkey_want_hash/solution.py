from pwn import *
import hashlib

HOST = "10.154.0.4"
PORT = 31479
conn = remote(HOST, PORT)

res = conn.recv().decode().strip()
print("Plaintext: " + res)

ans = hashlib.sha512(res.encode('utf-8')).hexdigest()
conn.sendline(ans.encode())

# Bit janky, not sure if this is a me or challenge problem.
conn.sendline()
conn.recvline()
conn.sendline()
print(conn.recvline().decode())
