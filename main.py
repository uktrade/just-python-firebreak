#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer

hostname = "localhost"
serverPort = 8080

class ApiServer(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes("<html><head><title>API Web Server</title></head>", "utf-8"))
    self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
    self.wfile.write(bytes("<body>", "utf-8"))
    self.wfile.write(bytes("<p>Server is running.</p>", "utf-8"))
    self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
  webServer = HTTPServer((hostname, serverPort), ApiServer)
  print("Server started http://%s:%s CTRL+C to stop..." % (hostname, serverPort))

  try:
      webServer.serve_forever()

  except KeyboardInterrupt:
      print("KeyboardInterrupt has been caught.")