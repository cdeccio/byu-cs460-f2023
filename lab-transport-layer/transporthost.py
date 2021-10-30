from headers import IPv4Header, UDPHeader, TCPHeader, \
        IP_HEADER_LEN, UDP_HEADER_LEN, TCP_HEADER_LEN, \
        TCPIP_HEADER_LEN, UDPIP_HEADER_LEN

from host import Host

class TransportHost(Host):
    def __init__(self, *args, **kwargs):
        super(TransportHost, self).__init__(*args, **kwargs)

        self.socket_mapping_udp = {}
        self.socket_mapping_tcp = {}

    def handle_tcp(self, pkt):
        pass

    def handle_udp(self, pkt):
        pass

    def install_socket_udp(self, local_addr, local_port, sock):
        self.socket_mapping_udp[(local_addr, local_port)] = sock

    def install_listener_tcp(self, local_addr, local_port, sock):
        self.socket_mapping_tcp[(local_addr, local_port, None, None)] = sock

    def install_socket_tcp(self, local_addr, local_port,
            remote_addr, remote_port, sock):
        self.socket_mapping_tcp[(local_addr, local_port, \
                remote_addr, remote_port)] = sock

    def no_socket_udp(self, pkt):
        pass

    def no_socket_tcp(self, pkt):
        pass
