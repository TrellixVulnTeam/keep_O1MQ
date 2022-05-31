from http.server import HTTPServer, BaseHTTPRequestHandler, ThreadingHTTPServer
from socketserver import ThreadingMixIn, ForkingMixIn
import threading


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        message = threading.currentThread().getName()
        self.wfile.write(message.encode("utf-8"))
        self.wfile.write(b"\n")


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True


class ForkingHTTPServer(ForkingMixIn, HTTPServer):
    pass


if __name__ == "__main__":
    # server = ThreadedHTTPServer(('localhost', 8080), Handler)
    server = ForkingHTTPServer(("localhost", 8080), Handler)
    print("Starting server, use <Ctrl+C> to stop")
    server.serve_forever()
