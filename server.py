import http.server
import socketserver
import os
import webbrowser
import sys

PORT = 8090
DIRECTORY = './web'

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super(CORSRequestHandler, self).end_headers()

def open_browser():
    url = f"http://localhost:{PORT}"
    print(f"Attempting to open browser to {url}")
    try:
        webbrowser.open(url)
        print("Browser opened successfully.")
    except Exception as e:
        print(f"Could not open browser: {e}")
        print(f"Please manually navigate to {url}")

def main():
    # Change to the specified directory
    os.chdir(DIRECTORY)

    with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
        print(f"Server started at http://localhost:{PORT}")
        print(f"Serving files from directory: {DIRECTORY}")
        
        if not sys.stdin.isatty():
            print("Running in a non-interactive environment. Skipping browser opening.")
        else:
            open_browser()
        
        print("Press Ctrl+C to stop the server.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    main()
