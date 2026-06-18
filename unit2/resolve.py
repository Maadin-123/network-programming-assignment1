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

# Test Cases
print("--- Q1: DNS Resolver Results ---")
print("Forward DNS (google.com):", resolve_hostname("google.com"))
print("Reverse DNS (8.8.8.8):", resolve_ip("8.8.8.8"))
print("Invalid Test (fake.domain):", resolve_hostname("fake.domain.invalid"))
