from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

port = 7777

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def get_params(self, name):
        qs = self.path[self.path.find("?")+1:]
        params = parse_qs(qs)
        values = params.get(name)

        return "" if values is None else values.pop()  #파이썬식 문법. 밑에 if문이랑 같은 뜻
        # if(values is None):
        #     return ""
        # else:
        #     return values.pop()

    def ex1(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()  # 응답 헤더
        self.wfile.write("<h1>안녕</h1>".encode("utf-8"))  # 응답 바디

    def ex2(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()  # 응답 헤더
        self.wfile.write("<h1>안녕안녕</h1>".encode("utf-8"))  # 응답 바디

    def do_GET(self):
        index = self.path.find("?")
        req_url = self.path if index == -1 else self.path[:index]

        #url mapping
        if(req_url == "/iot"):
            handler_name = "ex" + self.get_params("ex")
            #print(handler_name)
            if handler_name not in MyHTTPRequestHandler.__dict__:
                self.send_error(404, "File Not Found")
                return

            MyHTTPRequestHandler.__dict__[handler_name](self)

            # self.send_response(200)
            # self.send_header("Content-Type", "text/html; charset=utf-8")
            # self.end_headers()                                         # 응답 헤더
            # self.wfile.write("<h1>TEST</h1>".encode("utf-8"))          # 응답 바디

        elif(req_url == "board"):
            pass
        else:
            self.send_error(404, "File Not Found")

# http://localhost:7777/iot?ex=1
# http://localhost:7777/iot?ex=2
# http://localhost:7777/iot?ex=3

httpd = HTTPServer(("", port), MyHTTPRequestHandler)
print("Server running on port", port)
httpd.serve_forever()

