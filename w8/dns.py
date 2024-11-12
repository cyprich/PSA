#!/usr/bin/env python3

import socket as s
import struct

DNS_IP = "8.8.8.8"
DNS_PORT = 53
TRANSACTION_ID = 0x1234


def create_dns_query(domain_query: str) -> bytes:
    """
    create dns header
    1. transaction id
    2. flags
    3. questionsNo
    4. answersNo
    5. authorityNo
    6. additionalNo
    """

    flags = 0x0100  # = query
    out_bytes = struct.pack(
        "!6H", TRANSACTION_ID, flags, 1, 0, 0, 0
    )  # 6 dvojbajtovych policok

    """
    create dns query
    """

    labels = domain_query.split(".")

    for label in labels:
        out_bytes += struct.pack("!B", len(label))
        out_bytes += label.encode()

    out_bytes += struct.pack("!B", 0)
    # out_bytes += bytes(0x00)  # toto robi to iste co riadok predtym

    query_type = 1  # A record
    out_bytes += struct.pack("!2H", query_type, 1)

    return out_bytes


def parse_received_dns(recv_data, recv_ip, recv_port) -> bool:
    # data not received from server query was to`
    if recv_ip != DNS_IP or recv_port != DNS_PORT:
        return False

    # FIRST 2 BYTES: recv dns does not have the same transaction id as query
    if recv_data[0:2] != struct.pack("!H", TRANSACTION_ID):
        return False

    # SECOND 2 BYTES: this dns is not standard response without errors
    if recv_data[2:4] != struct.pack("!H", 0x8180):
        return False

    """
    # BYTES 7-8: this dns does not have 1 answer
    if recv_data[6:8] != struct.pack("!H", 1):
        return False
    """

    # BYTES 7-8: this dns does not have at least 1 answer
    answer_no = struct.unpack("!H", recv_data[6:8])[0]
    if answer_no < 1:
        return False

    # LAST 4 BYTES: ipv4 address
    # ntoa = network to address - bytes to string
    resp_ipv4 = s.inet_ntoa(recv_data[-4:])
    print(f"Response address: {resp_ipv4}")

    return True


if __name__ == "__main__":
    sock = s.socket(s.AF_INET, s.SOCK_DGRAM)

    query = str(input("Enter DNS record to resolve: "))

    # send dns query
    dns = create_dns_query(query)
    sock.sendto(dns, (DNS_IP, DNS_PORT))

    while True:
        # read dns response
        (buffer, (recv_ip, recv_port)) = sock.recvfrom(1000)

        # if dns response was found and is ok, quit
        if parse_received_dns(buffer, recv_ip, recv_port):
            break

        print("Ignoring Message: Not a correct one...")

    sock.close()
