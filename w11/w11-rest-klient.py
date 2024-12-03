#!/usr/bin/python3
import requests

USER = 'admin'
PASS = 'admin'
MIKROTIK_IP = "158.193.152.227"


def get_interfaces():
    url = f"http://{MIKROTIK_IP}/rest/interface"
    resp = requests.get(url, auth=(USER, PASS), verify=False)  # verify=False pri https

    out = list()

    if resp.status_code == 200:
        for interface in resp.json():
            out.append(interface["name"])
    return out


def get_ips(): 
    url = f"http://{MIKROTIK_IP}/rest/ip/address"
    resp = requests.get(url, auth=(USER, PASS), verify=False)  # verify=False pri https

    out = list()

    if resp.status_code == 200:
        for interface in resp.json():
            out.append({
                "int": interface["interface"],
                "ip": interface["address"]
            })
        
    return out


def get_ip_int():
    interfaces = get_interfaces()
    ips = get_ips()

    out = list()
    
    for interface in interfaces:
        out.append({'name': interface, 'ip': ""})

    for interface in out:
        for ip in ips:
            if interface["name"] == ip["int"]:
                interface["ip"] = ip["ip"]

    return out


def set_ip(iface: str, ip: str):
    url = f"http://{MIKROTIK_IP}/rest/ip/address"
    body = {"interface": iface, "address": ip}
    resp = requests.put(url, auth=(USER, PASS), verify=False, json=body)  # verify=False pri https

    if resp.status_code == 201:
        print(resp.json())
        return True

    print(resp.json())
    return False


if __name__ == "__main__":
    print(get_ip_int())
    set_ip("lo-Cyprich", "192.0.0.14/32")
    print("\n")
    print(get_ip_int())

