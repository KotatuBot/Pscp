from paramiko import SSHClient,AutoAddPolicy
from scp import SCPClient

from scp_get import Scp_Get
from scp_file_path import Copy_File_Path


HOST = "192.168.10.77"
PORT = 22
USER = "pi"
Password = "asdf4jkl;8"
ssh = SSHClient()
cfp = Copy_File_Path()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(hostname=HOST,port=PORT,username=USER,password=Password)
scp = SCPClient(ssh.get_transport())
scp_get = Scp_Get(ssh,scp)
remote_path = '/home/pi/TEST'
data = scp_get.get_data(remote_path)
local_path = "/Users/tatsuyakonishi/Documents/Lok"
cfp = Copy_File_Path()
remote_copy_file,local_create_dir,local_file_path = cfp.get_path(remote_path,local_path,data)
scp_get.local_create_dir(local_create_dir)
scp_get.local_create_file(remote_copy_file,local_file_path)




scp.close()
ssh.close()

