import socket
from tcp_protocol import CHAT_PROTOCOL, CONTROL_INFO

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999

if __name__ == "__main__":
    login = str(input("Enter your login name: "))
    protocol = CHAT_PROTOCOL(login)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_IP, SERVER_PORT))
    
    sock.send(protocol.login())
    print("Commands: \n\t_x: exit\n\t_u: list users")

    while True:
        command = str(input("Enter message or command: "))

        if command[0] == "_":
            match command[1]:
                case "x":
                    sock.send(protocol.logout())
                    sock.close()
                    exit()
                case "u":
                    sock.send(protocol.get_users())
                    msg_bytes = sock.recv(1000)
                    users = msg_bytes.decode()
                    print(users)
                    continue
                    
        else: 
            sock.send(protocol.send_text(command))


