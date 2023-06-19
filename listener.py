import socket
from gndp import get_passcode, get_host
from statements import *
from createfile import create_file

HOST = get_host()  # The IP address of the receiver
passcode = get_passcode(HOST)
PORT = 8080  # The port on which to communicate

printp(f"Passcode: {passcode}")

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))

        server.listen()
        printg(f"Listening on {HOST}:{PORT}")

        conn, addr = server.accept()

        filename = b''
        filedata = b''

        while True:
            data = conn.recv(1024)
            if not data: break
            
            if(not filename):
                filename = data
            else:
                filedata += data

        filename = filename.decode()
        
        printg(f"Received file: {filename}")

except Exception as e:
    print(f"An error occurred: {e}")

path = r"C:\Users\asuuj\Downloads"
create_file(path, filename, filedata)