from netmiko import ConnectHandler 

USER = 'admin'
PASS = 'admin'
CISCO_IP = "158.193.152.241"

conf = {
    "device_type": "cisco_ios",
    "host": CISCO_IP,
    "username": USER,
    "password": PASS
}

ssh = ConnectHandler(**conf)
ssh.set_command("show ip int b")

conf_commands = [
    "int lo1314",
    "ip add 192.0.0.14 255.255.255.255",
    "no shut"
]
ssh.send_config_set(conf_commands)
out = ssh.set_command("show ip int b")
print(out)


ssh.disconnect()
