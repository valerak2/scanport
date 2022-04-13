import threading
import socket
import queue


class Scanner:
    def __init__(self, host, port_range, timeout=0.2, workers=15):
        self.host = host
        self.ports = queue.Queue()
        for i in range(port_range[0], port_range[1] + 1):
            self.ports.put(i)

        socket.setdefaulttimeout(timeout)
        self.is_running = True

        self.threads = []
        for i in range(workers):
            self.threads.append(threading.Thread(target=self.run))

    def run(self):
        while self.is_running:
            try:
                port = self.ports.get(block=False)
            except queue.Empty:
                break
            self.get_tcp_port(port)

    def start(self):
        print('Scan started:')
        for thread in self.threads:
            thread.setDaemon(True)
            thread.start()

        for thread in self.threads:
            thread.join()

    def stop(self):
        self.is_running = False
        print('Scan stop')
        for thread in self.threads:
            thread.join()

    def get_tcp_port(self, port):
        my_socket = socket.socket()
        try:
            my_socket.connect((self.host, port))
        except socket.error or ConnectionResetError or ConnectionAbortedError:
            my_socket.close()
            return

        my_socket.send(b'aaa\r\n\r\n')
        try:
            data = my_socket.recv(1024)
            print(f'TCP {port} {self.list_protocol(data)}')
        except socket.timeout:
            pass
        except ConnectionResetError or ConnectionAbortedError:
            pass

        my_socket.close()

    @staticmethod
    def list_protocol(data):
        if b'SMTP' in data:
            return 'SMTP'
        if b'POP3' in data:
            return 'POP3'
        if b'SNTP' in data:
            return 'SNTP'
        if b'DNS' in data:
            return 'DNS'
        if b'HTTP' in data:
            return 'HTTP'
        return ''
