from paramiko import SSHClient,AutoAddPolicy
from scp import SCPClient

from scp_get import Scp_Get
from scp_put import Scp_put
from scp_file_path import Copy_File_Path


def get_dir(ssh,scp):
    scp_get = Scp_Get(ssh,scp)
    remote_path = ''
    data = scp_get.get_data(remote_path)
    local_path = ""
    cfp = Copy_File_Path()
    remote_copy_file,local_create_dir,local_file_path = cfp.get_path(remote_path,local_path,data)
    scp_get.local_create_dir(local_create_dir)
    scp_get.local_create_file(remote_copy_file,local_file_path)

def put_dir(ssh,scp):
    scp_put = Scp_put(ssh,scp)
    local_path = ""
    remote_path = ""
    local_copy_file,remote_create_dir,remote_file_path = scp_put.put_local_file(local_path,remote_path)
    scp_put.remote_mkdir(remote_create_dir)
    scp_put.remote_put(local_copy_file,remote_file_path)



HOST = ""
PORT = 
USER = ""
Password = ""
ssh = SSHClient()
cfp = Copy_File_Path()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(hostname=HOST,port=PORT,username=USER,password=Password)
scp = SCPClient(ssh.get_transport())
# getする
get_dir(ssh,scp)

scp.close()
ssh.close()

