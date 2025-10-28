"""
Cyber Escape Room server - Simple file server.
"""
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else int(os.environ.get('PORT', 8000))

class SimpleHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to all responses
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Accept')
        super().end_headers()

    def do_OPTIONS(self):
        # Handle CORS preflight requests
        self.send_response(204)  # No content
        self.end_headers()

    def do_GET(self):
        # Serve all files normally without protection
        return super().do_GET()

if __name__ == '__main__':
    addr = ('', PORT)
    print(f'Serving directory: {os.getcwd()}')
    print(f'Listening on http://0.0.0.0:{PORT}')
    httpd = HTTPServer(addr, SimpleHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nServer stopped')
        httpd.server_close()
