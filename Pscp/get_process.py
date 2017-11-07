import os
"""
リモートからローカル
にデータを処理するためのもの

リモート-->ローカル
"""

class Get_Process():
    def __init__(self,scp,ssh):
        self.ssh = ssh
        self.scp = scp

    def local_create_dir(self,local_dir_path):
        """
        ディレクトリを作成する関数
        """
        [os.mkdir(dir_path) for dir_path in local_dir_path]

    def local_create_file(self,remote_file_path,local_file_path):
        """
        ファイルを作成
        リモート-->ローカル
        """
        for number in range(len(local_file_path)):
            dirs = os.path.split(local_dir_path[number])[0]
            os.chdir(dirs)
            self.scp.get(remote_file_path)
