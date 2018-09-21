from http.server import BaseHTTPRequestHandler, HTTPServer

port = 8888

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()                                              # 응답 헤더

        self.wfile.write("<h1>안녕하세요</h1>".encode("utf-8"))          # 응답 바디


httpd = HTTPServer(("", port), MyHTTPRequestHandler)
print("Server running on port", port)
httpd.serve_forever()

