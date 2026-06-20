import ipaddress

def classify_ip(ip_string):
    try:
        ip = ipaddress.ip_address(ip_string.strip())
        return f"{ip_string} is an IPv{ip.version} address."
    except ValueError:
        return f"{ip_string} is an INVALID IP address."


