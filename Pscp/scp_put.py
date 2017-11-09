import subprocess
from scp_file_path import Copy_File_Path
class Scp_put():
    def __init__(self,ssh,scp):
        self.cfp = Copy_File_Path()
        self.ssh = ssh
        self.scp = scp

    def put_local_file(self,local_path,remote_path):
        command = ["ls","-R",local_path]
        result = subprocess.check_output(command)
        data = result.decode("utf-8")
        local_copy_file,remote_create_dir,local_file_path = self.cfp.get_path(local_path,remote_path,data)
        return local_copy_file,remote_create_dir,remote_file_path

    def remote_mkdir(self,local_create_dir):
        for dirs in local_create_dir:
            command = ["mkdir",dirs]
            result = subprocess.check_output(command)

    def remote_put(self,local_file,remote_copy_file):
        for number in range(len(local_file)):
            self.scp.put(local_file[number],remote_copy_file[number])



if __name__ == "__main__":
    sp = Scp_put()

