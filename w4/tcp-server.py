import socket
from enum import Enum

IP = "0.0.0.0"
PORT = 9999
USERS = []

"""
vlastny textovy protokol 😍
CHAT protocol v0.1a

|CONTROL_INFO|LOGIN|MESSAGE|

CONTROL_INFO types: LOGIN, DATA, LOGOUT, USERS
"""


class CONTROL_INFO(Enum):
    LOGIN = "LOGIN"
    DATA = "DATA"
    LOGOUT = "LOGOUT"
    USERS = "USERS"


class CHAT_PROTOCOL:
    def __init__(self, login: str):
        self._login: str = login
        self._msg_template: str = "|{0}|{1}|{2}|"

    def login(self) -> bytes:
        msg = self._msg_template.format(CONTROL_INFO.LOGIN, self._login, "")
        return msg.encode()

    def logout(self) -> bytes:
        msg = self._msg_template.format(CONTROL_INFO.LOGOUT, self._login, "")
        return msg.encode()

    def send_text(self, text: str) -> bytes:
        msg = self._msg_template.format(CONTROL_INFO.DATA, self._login, text)
        return msg.encode()

    def parse_msg(self, msg_bytes: bytes): 
        msg: str = msg_bytes.decode()
        (NULL, control, login, text, NULL) = msg.split("|")

        match control:
            case CONTROL_INFO.LOGIN:
                USERS.append(login)
                print(f"User {login} logged in")
                return True

            case CONTROL_INFO.LOGOUT:
                USERS.remove(login)
                print(f"User {login} logged out")
                return False

            case CONTROL_INFO.DATA:
                print(f"{login}: {text}\n")
                return True




if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((IP, PORT))
    sock.listen(10)

    protocol = CHAT_PROTOCOL("SERVER")

    while True:
        (client_sock, (client_addr, client_port)) = sock.accept()
        # print(f"Client connected {client_addr}:{client_port}")
        # print(f"Client connected {}:{}".format(client_addr, client_port))

        while True:
            buffer = client_sock.recv(1000)

            ret = protocol.parse_msg(buffer)
            if ret == False:
                client_sock.close()
                break

    sock.close()
