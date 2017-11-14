from paramiko import SSHClient,AutoAddPolicy
from scp import SCPClient

from scp_get import Scp_Get
from scp_put import Scp_put
from scp_file_path import Copy_File_Path
from commands import Command
from select_choice import select_Choice


class SSh_Connect():
    def __init__(self):
        self.ssh = ""
        self.scp = ""

    def get_dir(local_path,remote_path):
        scp_get = Scp_Get(self.ssh,self.scp)
        remote_copy_file,local_create_dir,local_file_path = scp_get.get_data(remote_path,local_path)
        scp_get.local_create_dir(local_create_dir)
        scp_get.local_create_file(remote_copy_file,local_file_path)

    def put_dir(local_path,remote_path):
        scp_put = Scp_put(self.ssh,self.scp)
        local_copy_file,remote_create_dir,remote_file_path = scp_put.put_local_file(local_path,remote_path)
        scp_put.remote_mkdir(remote_create_dir)
        scp_put.remote_put(local_copy_file,remote_file_path)

    def connect(Host,USER,Password):
        self.ssh = SSHClient()
        self.ssh.set_missing_host_key_policy(AutoAddPolicy())
        self.ssh.connect(hostname=HOST,port=22,username=USER,password=Password)
        self.scp = SCPClient(ssh.get_transport())

    def close(ssh,scp):
        self.scp.close()
        self.ssh.close()

