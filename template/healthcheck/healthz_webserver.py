import http.server

class HealthzHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != '/healthz':
            self.send_response(404)
            self.send_header("Content-length", "0")
            self.end_headers()
            return

        content = b'err'
        try:
            with open('/tmp/healthz', 'rb') as fd:
                content = fd.read().strip()
        except:
            pass
        self.send_response(200 if content == b'ok' else 400)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

httpd = http.server.HTTPServer(('', 45281), HealthzHandler)
httpd.serve_forever()
