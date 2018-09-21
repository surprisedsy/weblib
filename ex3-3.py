#POST 방식

from urllib.parse import urlencode
from urllib.request import Request, urlopen

data = urlencode({"name" : "둘리", "email" : "", "pwd" : ""})
data = data.encode("UTF-8")
print(data)

request = Request("http://www.example.com/join", data)
request.add_header("Content-Type", "text/html")

f = urlopen(request)
response = f.read()

print(response)