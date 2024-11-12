#!/usr/bin/env python3

from scapy.all import *


def mac_to_bytes(mac: str) -> bytes:
    mac = mac.replace(":", "")
    return bytes.fromhex(mac)


def compute_cdp_checksum(cdp_bytes: bytes):
    # TODO
    return 0


class Eth_frame:
    def __init__(self, src_mac: str):
        self._dst_mac: str = "01:00:0c:cc:cc:cc"
        self._src_mac: str = src_mac
        self._length: int = 0
        self._payload: Any = ""

    def add_payload(self, payload: Any):
        self._payload = payload

    def to_bytes(self) -> bytes:
        payload_bytes: bytes = self._payload.to_bytes()
        self._length = len(payload_bytes)

        eth_bytes = (
            mac_to_bytes(self._dst_mac)
            + mac_to_bytes(self._src_mac)
            + struct.pack("!H", self._length)
            + payload_bytes
        )
        return eth_bytes


# specificke llccko pre cdpcko
class LLC:
    def __init__(self):
        self._dsap: int = 0xAA
        self._ssap: int = 0xAA
        self._ctrl: int = 0x03
        self._oui: str = "00000C"
        self._pid: int = 0x2000
        self._payload: Any = ""

    def add_payload(self, payload: Any):
        self._payload = payload

    def to_bytes(self):
        return (
            struct.pack("!3B", self._dsap, self._ssap, self._ctrl)
            + mac_to_bytes(self._oui)
            + struct.pack("!H", self._pid)
            + self._payload.to_bytes()
        )


class CDP_header:
    def __init__(self):
        self._version: int = 1
        self._ttl: int = 180
        self._checksum: int = 0
        self._payload: List[Any] = []

    def add_payload(self, payload: Any):
        self._payload.append(payload)

    def to_bytes(self):
        cdp_bytes = struct.pack("!BBH", self._version, self._ttl, self._checksum)

        for i in self._payload:
            cdp_bytes += i.to_bytes()

        cdp_checksum = compute_cdp_checksum(cdp_bytes)
        return cdp_bytes[:2] + struct.pack("!H", cdp_checksum) + cdp_bytes[4:]


class TLV:
    def __init__(self, type):
        self._type = type
        self._length = 4

    def to_bytes(self):
        return struct.pack("!HH", self._type, self._length)


class Device_ID_TLV(TLV):
    def __init__(self, hostname: str):
        # super().__init__(hostname)
        TLV.__init__(self, 0x0001)
        self._hostname = hostname

    def to_bytes(self):
        hostname_bytes = self._hostname.encode()
        self._length += len(hostname_bytes)
        return super().to_bytes() + hostname_bytes


class Software_TLV(Device_ID_TLV):
    def __init__(self, software_version: str):
        super().__init__(software_version)
        self._type = 0x0005


class Platform_TLV(Device_ID_TLV):
    def __init__(self):
        super().__init__("PSA")
        self._type = 0x0006


def set_bit(in_var: Any, bit_number: int):
    return in_var | (1 << (bit_number - 1))


class Capabilities_TLV(TLV):
    def __init__(self, router=False, swich=False, host=True):
        TLV.__init__(self, 0x0004)
        self._length += 4
        self._capabilities = 0


if __name__ == "__main__":
    IFACES.show()

    # sys  3  wlo1  AzureWaveTec:41:a1:69  172.20.53.194  fe80::5800:d47:d96c:7f72
    # 10:68:38:41:a1:69

    iface = IFACES.dev_from_index(3)
    sock = conf.L2socket(iface=iface)

    eth = Eth_frame("10:68:38:41:a1:69")
    llc = LLC()
    cdp = CDP_header()

    tlv_dev = Device_ID_TLV("arch")
    cdp.add_payload(tlv_dev)

    tlv_soft = Software_TLV("Arch Linux x86_64")
    cdp.add_payload(tlv_soft)

    tlv_platform = Platform_TLV()
    cdp.add_payload(tlv_platform)

    llc.add_payload(cdp)

    eth.add_payload(llc)
    eth_bytes = eth.to_bytes()

    sock.send()
