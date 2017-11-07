import os
from scp_file_path import Copy_File_Path

"""
リモートからローカルに
データを取得する関数
"""

class Scp_Get():
    def __init__(self,ssh,scp):
        self.scp = scp
        self.ssh = ssh

    def get_data(self,remote_path):
        command = 'ls -R {0}'.format(remote_path).encode("utf-8")
        stdin, stdout, stderr = ssh.exec_command(command)
        data = stdout.read().decode("utf-8")
        print(data)
        return data
