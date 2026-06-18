import socket

def resolve_hostname(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return "Error: Unable to resolve hostname."

def resolve_ip(ip_address):
    try:
        return socket.gethostbyaddr(ip_address)
    except (socket.herror, socket.gaierror):
        return "Error: Unable to resolve IP address."


