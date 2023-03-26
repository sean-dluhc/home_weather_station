import socket
from get_weather_data import get_data


# Define socket host and port
SERVER_HOST = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 8000
print(SERVER_HOST)

# Create socket
def create_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print('Listening on port %s ...' % SERVER_PORT)
    print(server_socket)
    return server_socket


def get_client_connections(server_socket):
    # Wait for client connections
    client_connection, client_address = server_socket.accept()
    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)
    return client_connection


def send_response(html, client_connection):
    response = b'HTTP/1.1 200 OK\r\n'
    response += b'Content-Type: text/html\r\n'
    response += b'Content-Length: ' + str(len(html)).encode('utf-8') + b'\r\n'
    response += b'\r\n'
    response += html
    client_connection.send(response)
    client_connection.close()
    

def generate_html():
    html_content = f"""
                <!DOCTYPE html>
                <html>
                <head>
                <title>Weather Station</title>
                <meta http-equiv="refresh" content="10">
                </head>
                <body>
                <p>{get_data()}r</p>
                </body>
                </html>
                """.encode('utf-8')
    return(html_content)

server = create_socket()

while True:    
        client_con = get_client_connections(server_socket=server)
        send_response(html=generate_html(), client_connection=client_con)

