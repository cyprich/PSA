from paramiko import SSHClient, AutoAddPolicy

USER = 'admin'
PASS = 'admin'
CISCO_IP = "158.193.152.241"
MIKROTIK_IP = "158.193.152.227"

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())

ssh.connect(hostname=MIKROTIK_IP, username=USER, password=PASS)
(stdin, stdout, stderr) = ssh.exec_command("/interface bridge add name=lo-Cyprich")

ssh.connect(hostname=MIKROTIK_IP, username=USER, password=PASS)
(stdin, stdout, stderr) = ssh.exec_command("/interface print terse")

out = list()
for line in stdout:
    parsed = line.strip("\n").strip("\r").split(" ")

    if len(parsed) > 1:
        parsed = parsed[2:]

        for item in parsed:
            prvok = item.split("=")

            if prvok[0] == "name":
                out.append(prvok[1])

print(out)

