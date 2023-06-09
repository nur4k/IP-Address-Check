import socket

def get_ip_by_hostname():
    hostname = input("Enter website address(URL): ")

    try:
        return f'Hostname: {hostname}\nIP Address: {socket.gethostbyname(hostname)}'
    except socket.gaierror as error:
        return f'Hostname invalid {error}'

def main():
    print(get_ip_by_hostname())

if __name__ == '__main__':
    main()