import socket


def port_scanner(domain):
    common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 993, 995]

    print(f"🔍 Scanning {domain} with just sockets...")

    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((domain, port))
        if result == 0:
            print(f" Port {port}: OPEN")

            # Try to get service banner
            try:
                sock.settimeout(2)
                banner = sock.recv(1024).decode('utf-8', errors='ignore')
                if banner:
                    print(f" Banner: {banner.strip()[:100]}...")
            except:
                pass
        else:
            print(f" Port {port}: CLOSED")

        sock.close()


port_scanner("yourwebsite.com")