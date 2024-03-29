from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os, socket



def get_ip_address():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Try connecting to a public server (Google's DNS server)
        s.connect(("8.8.8.8", 80))

        # Get the local IP address of the computer
        ip_address = s.getsockname()[0]
    except Exception as e:
        print(f"Error Getting IPv4 address of the machine: {e}")
        ip_address = None
    finally:
        # Close the socket
        s.close()

        return ip_address


def start_server(htmlpath, host, port):
    try:
        # Get the directory of the HTML file
        filepath = os.path.dirname(os.path.realpath(htmlpath))

        # Change the current working directory to the HTML file directory
        os.chdir(filepath)

        # Create the HTTP server
        server_address = (host, port)
        httpd = TCPServer(server_address, SimpleHTTPRequestHandler)
        print(f"Server running at http://{host}:{port}")

        # Start the server
        httpd.serve_forever()
    except Exception as e:
        print(f"Error Starting Server: {e}")


