import socket
import psutil

def get_local_host_info():
    print("=== Local Host Information ===")
    
    hostname = socket.gethostname()
    print(f"Hostname: {hostname}")
    
    interfaces = psutil.net_if_addrs()
    
    print("\n--- Network Interfaces ---")
    for intf_name, addresses in interfaces.items():
        print(f"\nInterface: {intf_name}")
        
        ipv4_addresses = []
        mac_address = "Not Found"
        
        for addr in addresses:
            if addr.family == psutil.AF_LINK:
                mac_address = addr.address
            elif addr.family == socket.AF_INET:
                ipv4_addresses.append(addr.address)
        
        print(f"  MAC Address:  {mac_address}")
        if ipv4_addresses:
            print(f"  IP Address:   {', '.join(ipv4_addresses)}")
        else:
            print("  IP Address:   No active IPv4 address")

if __name__ == "__main__":
    get_local_host_info()
