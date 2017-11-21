import subprocess
import re
import os

class Copy_File_Path():
    def __init__(self):
        pass

    def file_path_dir(self,root_dir,remote_data,local_path):
        """
        ファイルリストのリストを作成
        する

        Args:
            root_dir:ルートディレクトリ名
            remote_data:リモートデータ
            local_path:ローカルのファイルパス

        """
        # リモートのファイルのパス
        remote_copy_file = []
        # 作成するローカルのディレクトリファイルパス
        local_create_dir = []
        # 作成するローカルのファイルパス
        local_file = []
        root_dir = "/"+root_dir
        for j in remote_data:
            result = j.split(":")
            dir_name = result[0]
            if len(result) is 2 and result[1] is not "":
                file_names = result[1].strip()
                # dir_nameに対するファイルパスを作成する
                file_list = file_names.split("\n")
                for file_name in file_list:
                    file_list = file_name.split("/")
                    if len(file_list)!=2:
                        origin_file = os.path.join(dir_name,file_name)
                        test = dir_name+"/"
                        under_dir_name = test.split(root_dir+"/")[1]
                        if under_dir_name == "":
                            local_file_path = local_path + root_dir + under_dir_name +"/"+file_name
                        else:
                            local_file_path = local_path + root_dir + "/" + under_dir_name + file_name
                        local_file.append(local_file_path)
                        remote_copy_file.append(origin_file)
            test = dir_name + "/"
            under_path = test.split(root_dir+"/")[1]
            dir_path = local_path + root_dir +"/"+under_path
            # コピー先のディレクトリパスを作成
            local_create_dir.append(dir_path)
        return remote_copy_file,local_create_dir,local_file 

    def pattern_search(self,data,local_path):
        """
        ファイルが存在するかを判断する関数
        """
        repattern = re.compile(r".*:")
        hits = repattern.match(data[0])
        # もしひとつ目が:でないならば
        if hits is None:
            data = [local_path+":\n"+data[0]]+data[1:]
        return data

    def get_root_dir(self,path):
        """
        ルートとなるファイルパスを取得する関数
        """
        root_dir = path.split("/")[-1]
        return root_dir

    def get_path(self,remote_path,local_path,data):
        """
        ファイルパスを取得する関数

        Args: 
            remote_path:リモートのファイルパス
            local_path:ローカルのファイルパス

        return:
            remote_copy_file: リモートのファイルのパス
            local_create_dir: ローカルのディレクトリパス
            local_file_path: ローカルのファイルパス
        """
        data = data.strip()
        results = data.split("\n\n")
        files_data = self.pattern_search(results,remote_path)
        root = self.get_root_dir(remote_path)
        remote_copy_file,local_create_dir,local_file_path = self.file_path_dir(root,files_data,local_path)
        return remote_copy_file,local_create_dir,local_file_path 

if __name__ == "__main__":
    cfp = Copy_File_Path()
     
