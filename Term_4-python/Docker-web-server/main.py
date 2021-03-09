from http.server import HTTPServer, BaseHTTPRequestHandler
import os


def load_binary(file):
    with open(file, 'rb') as file:
        return file.read()


class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        path = os.path.join('/webpage', self.path[1:])
        print(f'Path to open : {path}')
        try:
            file_to_open = load_binary(path[1:])
            self.send_response(200)
        except:
            file_to_open = 'no such webpage'.encode()
            self.send_response(404)
        self.end_headers()
        self.wfile.write(file_to_open)



def main():
    port = 8000
    server = HTTPServer(('0.0.0.0', port), helloHandler)
    print(f'Server running on port {port}')
    server.serve_forever()


if __name__ == '__main__':
    main()
