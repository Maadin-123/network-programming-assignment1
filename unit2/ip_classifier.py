import ipaddress

def classify_ip(ip_string):
    try:
        ip = ipaddress.ip_address(ip_string.strip())
        return f"{ip_string} is an IPv{ip.version} address."
    except ValueError:
        return f"{ip_string} is an INVALID IP address."

# Test Cases
print(classify_ip("192.168.1.1"))
print(classify_ip("2001:db8::1"))
print(classify_ip("999.999.999.999"))
