from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()

    def do_GET(self):
        # Serve index.html for root path
        if self.path == '/':
            self.path = '/loja.html'
        return super().do_GET()

if __name__ == '__main__':
    port = 8000
    print(f"Servidor rodando em http://localhost:{port}")
    httpd = HTTPServer(('localhost', port), CORSRequestHandler)
    httpd.serve_forever() 