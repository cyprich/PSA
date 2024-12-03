from paramiko import SSHClient, AutoAddPolicy

USER = 'admin'
PASS = 'admin'
CISCO_IP = "158.193.152.241"
MIKROTIK_IP = "158.193.152.227"

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(hostname=CISCO_IP, username=USER, password=PASS)
(stdin, stdout, stderr) = ssh.exec_command("show ip int b")

out = list()
for line in stdout:
    parsed = line.strip("\n").strip("\r").split(" ")
    parsed = parsed[0]

    out.append(parsed[0])

out.pop(0)
out.pop(0)
print(out)
