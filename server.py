import socket 
import threading
# TCP Client Handler
def handle_tcp_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"TCP Received: {message}")
            # Echo back the message to the client
            client_socket.send(f"TCP Echo: {message}".encode())
        except ConnectionResetError:
            break
    client_socket.close()
# UDP Server Handler
def udp_server(udp_socket):
    while True:
        message, addr = udp_socket.recvfrom(1024)
        print(f"UDP Received from {addr}: {message.decode()}")
        # Send a reply back to the client
        udp_socket.sendto(f"UDP Echo: {message.decode()}".encode(), addr)
# Server Setup
def start_server():
    # TCP Server setup
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind(('0.0.0.0', 9999))
    tcp_server.listen(5)
    print("TCP Server listening on port 9999...")
    # UDP Server setup
    udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server_socket.bind(('0.0.0.0', 9998))
    print("UDP Server listening on port 9998...")
    # Start the UDP server in a separate thread
    udp_thread = threading.Thread(target=udp_server, args=(udp_server_socket,))
    udp_thread.start()
    # Handle incoming TCP connections
    while True:
        client_socket, addr = tcp_server.accept()
        print(f"TCP Connection from {addr}")
        client_handler = threading.Thread(target=handle_tcp_client, args=(client_socket,))
        client_handler.start()
if __name__ == "__main__":
    start_server()