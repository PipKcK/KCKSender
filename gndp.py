import socket

def get_host():
    IPS = socket.gethostbyname(socket.gethostname())
    return IPS

def get_passcode(IPS):
    encoded_IPS = ""
    for char in IPS:
        ascii_val = ord(char)
        encoded_char = chr((ascii_val + 26) % 256)
        encoded_IPS += encoded_char
    return encoded_IPS

def decode_passcode(eIPS):
    decoded_eIPS = ""
    for char in eIPS:
        ascii_val = ord(char)
        temp = chr((ascii_val - 26) % 256)
        decoded_eIPS += temp
    return decoded_eIPS



