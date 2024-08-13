import socket

print ("""
████████╗██████╗ ███████╗██╗  ██╗ █████╗ ███████╗
╚══██╔══╝██╔══██╗██╔════╝╚██╗██╔╝██╔══██╗██╔════╝
   ██║   ██████╔╝█████╗   ╚███╔╝ ███████║███████╗
   ██║   ██╔══██╗██╔══╝   ██╔██╗ ██╔══██║╚════██║
   ██║   ██║  ██║███████╗██╔╝ ██╗██║  ██║███████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                                                 """)

def get_server_info(ip):
    try:
        server_ip = socket.gethostbyname(ip)
        port = 80  # Standard HTTP-Port, kann geändert werden

        print("\n--- Server Information ---")
        print(f"IP Address: {server_ip}")
        print(f"Suggested Port: {port}")
    except socket.gaierror:
        print("Invalid IP address or domain name!")

def main():
    print("Enter the IP address or domain name of the server:")
    server_ip = input("IP/Domain: ")
    get_server_info(server_ip)

if __name__ == "__main__":
    main()
