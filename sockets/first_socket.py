import socket # For socket


try:
    # Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET for address family ipv4 and SOCK_STREAM for connection oriented TCP protocol
except socket.error as error:
    print("Socket creation failed with error %s" %(error)) # Print socket error

port = 80

try:
    ip  = socket.gethostbyname("www.google.com") # Get IP address
    print(ip)
except socket.gaierror: # gaierror means GetAddrInfo()

    # This means could not resolve the host
    print("Could not resolve host")
    sys.exit()
