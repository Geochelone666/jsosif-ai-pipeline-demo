"""Exercise the real HTTP redirect handler without any external API or secret."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from urllib.error import HTTPError
from urllib.request import Request

import pytest
from credential_http import urlopen


def test_authenticated_redirect_is_never_followed():
    received = []
    class Handler(BaseHTTPRequestHandler):
        def do_POST(self):
            received.append(self.path)
            self.send_response(307)
            self.send_header('Location', '/credential-sink')
            self.end_headers()
        def do_GET(self):
            received.append(self.path)
            self.send_response(200)
            self.end_headers()
        def log_message(self, *args):
            pass
    server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        request = Request(f'http://127.0.0.1:{server.server_port}/provider', data=b'{}',
                          headers={'Authorization': 'Bearer synthetic-key'})
        with pytest.raises(HTTPError) as exc:
            urlopen(request, timeout=3)
        assert exc.value.code == 307
        assert received == ['/provider']
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
