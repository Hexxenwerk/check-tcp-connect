import socket
import sys


def tcp_connect(target: dict):
    try:
        socket.create_connection((target["host"], target["port"]), 30)
        print(f'Connection to {target["host"]} port {target["port"]} successful')
        return 0
    except TimeoutError:
        print(f'Connection to {target["host"]} port {target["port"]} timed out')
        return 3
    except ConnectionRefusedError:
        print(f'Connection to {target["host"]} port {target["port"]} refused')
        return 2
    except socket.error as e:
        print(f'Connection to {target["host"]} port {target["port"]} failed: {e}')
        return 2


def targets_from_arguments():
    targets: list = []
    for target in sys.argv[1:]:
        try:
            host, port = target.split(":")
        except ValueError:
            print(f'Parameter syntax error: "{target}"; Must be "<host>:<port>"')
            continue
        try:
            targets.append({
                "host": host,
                "port": int(port)
            })
        except ValueError:
            print(f'Port must be numeric: {port}')
            continue
    return targets


def main():
    exit_code = 0
    targets = targets_from_arguments()
    for target in targets:
        rc: int = tcp_connect(target)
        if rc > exit_code:
            exit_code = rc
    sys.exit(exit_code)


if __name__ == '__main__':
    # Main prog starts here
    main()
