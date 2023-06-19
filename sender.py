import socket
from gndp import decode_passcode
import os
from statements import *

passcode = input("Enter your password: ")
filepath = r'C:\Users\asuuj\Documents\VSCodes\Python\ReSEND\kitty.jpg'
PORT = 8080

HOST = decode_passcode(passcode)
filename = os.path.basename(filepath)

try:
    with open(filepath, 'rb') as file:
        filedata = file.read()
        file.close()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        try:
            client.connect((HOST, PORT))
        except Exception as e:
            printr("Incorrect Passcode or busy Port")
        client.send(filename.encode())
        client.sendall(filedata)
        client.close()

    printb(f"File: {filename} has been sent.")

except Exception as e:
    printr(f"An error occurred: {e}")
