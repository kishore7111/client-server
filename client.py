import socket
import threading
# TCP Client handler
def tcp_client():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect(('127.0.0.1', 9999))
    while True:
        message = input("TCP message: ")
        if message.lower() == "exit":
            break
        tcp_socket.send(message.encode())
        response = tcp_socket.recv(1024).decode()
        print(f"TCP Response: {response}")
    tcp_socket.close()
# UDP Client handler
def udp_client():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('127.0.0.1', 9998)
    while True:
        message = input("UDP message: ")
        if message.lower() == "exit":
            break
        udp_socket.sendto(message.encode(), server_address)
        response, _ = udp_socket.recvfrom(1024)
        print(f"UDP Response: {response.decode()}")
    udp_socket.close()
# Start client threads
def start_client():
    tcp_thread = threading.Thread(target=tcp_client)
    udp_thread = threading.Thread(target=udp_client)
    tcp_thread.start()
    udp_thread.start()
    tcp_thread.join()
    udp_thread.join()
if __name__ == "__main__":
    start_client()
