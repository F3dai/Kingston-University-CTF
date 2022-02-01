import pwnlib.util.web

if b"exploited" in pwnlib.util.web.wget("http://localhost:1337/vulnerable"):
      exit(0)

exit(1)
