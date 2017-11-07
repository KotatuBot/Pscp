from paramiko import SSHClient,AutoAddPolicy
from scp import SCPClient


HOST = "10.1.215.130"
PORT = 22
USER = "k919200"
Password = "kobakoba"
ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(hostname=HOST,port=PORT,username=USER,password=Password)
scp = SCPClient(ssh.get_transport())
path = '/home/k919200/TEST'
command = 'ls -R {0}'.format(path).encode("utf-8")
stdin, stdout, stderr = ssh.exec_command(command)
data = stdout.read()

scp.close()
ssh.close()

