from paramiko import SSHClient,AutoAddPolicy
from scp import SCPClient

from Pscp.scp_get import Scp_Get
from Pscp.scp_put import Scp_put
from Pscp.scp_file_path import Copy_File_Path
from Pscp.commands import Command


class SSh_Connect():
    def __init__(self):
        self.ssh = ""
        self.scp = ""

    def get_dir(self,remote_path,local_path):
        scp_get = Scp_Get(self.ssh,self.scp)
        remote_copy_file,local_create_dir,local_file_path = scp_get.get_data(remote_path,local_path)
        scp_get.local_create_dir(local_create_dir)
        scp_get.local_create_file(remote_copy_file,local_file_path)
        print("Finish Geting")

    def get(self,remote_path,local_path):
        scp_get = Scp_Get(self.ssh,self.scp)
        scp_get.one_file(remote_path,local_path)

    def put_dir(self,local_path,remote_path):
        scp_put = Scp_put(self.ssh,self.scp)
        local_copy_file,remote_create_dir,remote_file_path = scp_put.put_local_file(local_path,remote_path)
        scp_put.remote_mkdir(remote_create_dir)
        scp_put.remote_put(local_copy_file,remote_file_path)

    def put(self,local_path,remote_path):
        scp_put = Scp_put(self.ssh,self.scp)
        scp_put.one_remote_put(local_path,remote_path)

    def connect(self,HOST,USER,Password):
        self.ssh = SSHClient()
        self.ssh.set_missing_host_key_policy(AutoAddPolicy())
        self.ssh.connect(hostname=HOST,port=22,username=USER,password=Password)
        self.scp = SCPClient(self.ssh.get_transport())

    def close(self):
        self.scp.close()
        self.ssh.close()

