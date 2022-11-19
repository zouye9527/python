# 引入网络编程库
import http.server
import socketserver
#　启动服务器
Handler=http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("",8000),Handler) as httpd:
    print("serving at port", 8000)
    httpd.serve_forever()