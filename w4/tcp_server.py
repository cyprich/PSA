import socket
from tcp_protocol import CHAT_PROTOCOL, CONTROL_INFO
from threading import Thread


IP = "0.0.0.0"
PORT = 9999
USERS = []


# obsluhovanie jedneho klienta
def handle_client(client_sock):
    while True:
        buffer = client_sock.recv(1000)

        # (control, data) = protocol.parse_msg(buffer, USERS)
        parsed_message = protocol.parse_msg(buffer, USERS)
        control = parsed_message[0]

        if control == CONTROL_INFO.LOGOUT:
            client_sock.close()
            break

        elif control == CONTROL_INFO.USERS:
            users = parsed_message[1]
            client_sock.send(users.__str__().encode())
            continue


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((IP, PORT))
    sock.listen(10)

    protocol = CHAT_PROTOCOL("SERVER")

    # obsluhovanie vsetkych
    while True:
        (client_sock, (client_addr, client_port)) = sock.accept()
        print(f"Client connected {client_addr}:{client_port}")
        # print(f"Client connected {}:{}".format(client_addr, client_port))

        thread = Thread(target=handle_client, args=(client_sock,))
        thread.start()

    sock.close()
