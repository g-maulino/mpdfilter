#!/usr/bin/env python3
#
# DASH proxy - proxify MPEG DASH manifest requests for attributes filtering
#
#       Use the hardcoded HOST, PORT parametters to adapt
#
# Warning: Does not support Byte Range requests !
#
# Author: g-maulino
#
import http.server  
import socketserver
import sys
import urllib.request

from mpdfilters import MPDattfilter

HOST = "127.0.0.1"
PORT = 8080

class Proxy(http.server.SimpleHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        if(self.path.endswith('.mpd')):
            self.send_header("Content-type", "application/dash+xml")
        else:
            self.send_header("Content-type", "video/mp4")
        self.end_headers()

    def do_GET(self):
        print (self.path)
        print (self.headers)
        self._set_headers()

        stream_resp = urllib.request.urlopen('http://' + HOST + self.path)

        data = stream_resp.read()

        if (self.path.endswith('.mpd')):
            
            mp = MPDattfilter()
            data = mp.filter_r0(data)

        #self.copyfile(data, self.wfile)
        self.wfile.write(data)
        print ("--------------------------------------------\n")

def main() -> int:

    Handler = Proxy
    server = socketserver.TCPServer(('0.0.0.0', PORT), Handler)

    server.serve_forever()
    return 0

if __name__ == '__main__':
    sys.exit(main())  #