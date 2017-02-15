from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8080
auth={"Dheeraj:kumar"}
class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
    response = requests.get('Authorization', headers=auth)
       self.headers = {'Authorization': 'Basic' +auth}
       if Authorization == none or Authorization != auth :
        self.send_response(400)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("no auth")
        return
       else:
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Hi DHEERAJ")
       return
try:
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ', PORT_NUMBER
    server.serve_forever()
except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()