from enum import Enum

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
        msg = self._msg_template.format(CONTROL_INFO.LOGIN.value, self._login, "")
        return msg.encode()

    def logout(self) -> bytes:
        msg = self._msg_template.format(CONTROL_INFO.LOGOUT.value, self._login, "")
        return msg.encode()

    def send_text(self, text: str) -> bytes:
        msg = self._msg_template.format(CONTROL_INFO.DATA.value, self._login, text)
        return msg.encode()

    def get_users(self) -> bytes:
        msg = self._msg_template.format(CONTROL_INFO.USERS.value, self._login, "")
        return msg.encode()

    def parse_msg(self, msg_bytes: bytes, users: list):
        msg: str = msg_bytes.decode()
        (NULL, control, login, text, NULL) = msg.split("|")

        match control:
            case CONTROL_INFO.LOGIN.value:
                users.append(login)
                print(f"User {login} logged in")
                return (CONTROL_INFO.LOGIN, None)

            case CONTROL_INFO.LOGOUT.value:
                users.remove(login)
                print(f"User {login} logged out")
                return (CONTROL_INFO.LOGOUT, None)

            case CONTROL_INFO.USERS.value:
                return (CONTROL_INFO.USERS, users)

            case CONTROL_INFO.DATA.value:
                print(f"{login}: {text}\n")
                return (CONTROL_INFO.DATA, text)

        return (None, None)
