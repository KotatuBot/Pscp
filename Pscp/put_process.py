import subprocess

class Put_Process():
    def __init__(self,ssh,scp):
        self.ssh = ssh
        self.scp = scp

    def remote_mkdir(self,local_create_dir):
        for dirs in local_create_dir:
            command = ["mkdir",dirs]
            result = subprocess.check_output(command)

    def remote_put(self,local_file,remote_copy_file):
        for number in range(len(local_file)):
            self.scp.put(local_file[number],remote_copy_file[number])

    def put_file_data(self,local_path):
        command = ["ls","-R",remote_path]
        result = subprocess.check_output(command)
        data = result.decode("utf-8")
        data = data.strip()
        results = data.split("\n\n")
        return result

