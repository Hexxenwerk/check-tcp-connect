import socket


def tcp_connect(host: str, port: int):
    try:
        with socket.socket() as s:
            s.connect((host, port))
        print(f'Connection to {host} port {port} successful')
        return 0
    except TimeoutError:
        print(f'Connection to {host} port {port} timed out')
        return 3
    except ConnectionRefusedError:
        print(f'Connection to {host} port {port} refused')
        return 2
    except socket.error as e:
        print(f'Connection to {host} port {port} failed: {e}')
        return 2


def main():
    exit(tcp_connect("www.heise.de", 89))


if __name__ == '__main__':
    main()
