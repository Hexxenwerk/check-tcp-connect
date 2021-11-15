import socket


def tcp_connect(host: str, port: int):
    try:
        with socket.socket() as s:
            s.connect((host, port))
        print('Connection to {} port {} successful'.format(host, port))
        return 0
    except TimeoutError:
        print('Connection to {} port {} timed out'.format(host, port))
        return 3
    except ConnectionRefusedError:
        print('Connection to {} port {} refused'.format(host, port))
        return 2
    except socket.error as e:
        print('Connection to {} port {} failed: {}'.format(host, port, e))
        return 2


def main():
    exit(tcp_connect("www.heise.de", 89))


if __name__ == '__main__':
    main()
