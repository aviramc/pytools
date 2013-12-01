import socket
import ssl

def recv_until(socket_object, until, buffer_size=1024):
    accumulated_buffer = ''
    found = False
    while True:
        temp_buffer = socket_object.recv(buffer_size, socket.MSG_PEEK)
        if temp_buffer == '':
            break
        accumulated_buffer += temp_buffer
        find_index = accumulated_buffer.find(until)
        if find_index != -1:
            found = True
            
def create_ssl_connection(socket_object, address, port, *ssl_args, **ssl_kws):
    socket_object.connect((address, port))
    socket_object = ssl.wrap_socket(socket_object,
                                    *ssl_args,
                                    **ssl_kws
                                   )
    return socket_object

