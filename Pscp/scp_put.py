import subprocess
import os

import Pscp.scp_file_path as scp_file
class Scp_put():
    def __init__(self,ssh,scp):
        self.cfp = scp_file.Copy_File_Path()
        self.ssh = ssh
        self.scp = scp

    def put_local_file(self,local_path,remote_path):
        command = ["ls","-RF",local_path]
        result = subprocess.check_output(command)
        data = result.decode("utf-8")
        local_copy_file,remote_create_dir,local_file_path = self.cfp.get_path(local_path,remote_path,data)
        return local_copy_file,remote_create_dir,local_file_path

    def remote_mkdir(self,remote_create_dir):
        for dirs in remote_create_dir:
            command = "mkdir -p {dir_name}".format(dir_name=dirs).encode("utf-8")
            stdin, stdout, stderr = self.ssh.exec_command(command)

    def remote_put(self,local_file,remote_copy_file):
        for number in range(len(local_file)):
            remote_dir = os.path.split(remote_copy_file[number])
            self.scp.put(local_file[number],remote_dir[0])
        print("Finish puts")


    def one_remote_put(self,local_file_path,remote_copy_file):
        self.scp.put(local_file_path,remote_copy_file)


if __name__ == "__main__":
    sp = Scp_put()

