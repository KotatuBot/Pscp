import os

import Pscp.scp_file_path as scp_file

"""
リモートからローカルに
データを取得する関数
"""

class Scp_Get():
    def __init__(self,ssh,scp):
        self.ssh = ssh
        self.scp = scp
        self.cfp = scp_file.Copy_File_Path()

    def get_data(self,remote_path,local_path):
        command = 'ls -RF {0}'.format(remote_path).encode("utf-8")
        stdin, stdout, stderr = self.ssh.exec_command(command)
        data = stdout.read().decode("utf-8")
        remote_copy_file,local_create_dir,local_file_path = self.cfp.get_path(remote_path,local_path,data)
        return remote_copy_file,local_create_dir,local_file_path

    def local_create_dir(self,local_dir_path):
        """
        ディレクトリを作成する関数
        """
        for dir_path in local_dir_path:
            os.mkdir(dir_path)

    def local_create_file(self,remote_file_path,local_file_path):
        """
        ファイルを作成
        リモート-->ローカル
        """
        pwd = os.getcwd()
        for number,file_path in enumerate(local_file_path):
            file_list = file_path.split("/")
            file_name = file_list[-1]
            dirs_name = "/".join(file_list[:-1])
            os.chdir(dirs_name)
            self.scp.get(remote_file_path[number])
        os.chdir(pwd)

    def one_file(self,remote_file_path,local_file_path):
        pwd = os.getcwd()
        os.chdir(local_file_path)
        self.scp.get(remote_file_path)
        os.chdir(pwd)
