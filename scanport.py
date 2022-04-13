import sys
from scanner import Scanner
import argparse


def parser_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', action='store_true',
                        dest='tcp_scan',
                        required=True,
                        help='Scan to tcp ports.')

    parser.add_argument('-p', '--ports',
                        type=int, dest='port_range',
                        nargs=2, default=[1, 65535],
                        help='Scanned port range')

    parser.add_argument('host', help='Host to scan')

    return parser.parse_args()


def check_port_range(port_range):
    for port in port_range:
        if port < 1 or port > 65535:
            print('Invalid port value.')
            sys.exit(10)


def main(host, port_range):
    scanner = Scanner(host, port_range)
    try:
        scanner.start()
    except KeyboardInterrupt:
        scanner.stop()



if __name__ == '__main__':
    args = parser_arguments()
    check_port_range(args.port_range)
    try:
        main(args.host, sorted(args.port_range))
    except PermissionError:
        print("Permission error")
        sys.exit(11)
