import sys

from paramiko import SSHClient,AutoAddPolicy
from scp import SCPClient

from scp_get import Scp_Get
from scp_put import Scp_put
from scp_file_path import Copy_File_Path
from commands import Command
from select_choice import select_Choice


def get_dir(ssh,scp):
    scp_get = Scp_Get(ssh,scp)
    remote_path = ''
    local_path = ""
    remote_copy_file,local_create_dir,local_file_path = scp_get.get_data(remote_path,local_path)
    scp_get.local_create_dir(local_create_dir)
    scp_get.local_create_file(remote_copy_file,local_file_path)

def put_dir(ssh,scp):
    scp_put = Scp_put(ssh,scp)
    local_path = "/Users/tatsuyakonishi/Documents/Lok"
    remote_path = "/home/pi"
    local_copy_file,remote_create_dir,remote_file_path = scp_put.put_local_file(local_path,remote_path)
    #scp_put.remote_mkdir(remote_create_dir)
    #scp_put.remote_put(local_copy_file,remote_file_path)

def connect(Host,PORT,USER,Password):
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(hostname=HOST,port=PORT,username=USER,password=Password)
    scp = SCPClient(ssh.get_transport())

def close(ssh,scp):
    scp.close()
    ssh.close()

message  = """"  
              ________  ________  ________  ________
             |\   __  \|\   ____\|\   ____\|\   __  \  
             \ \  \|\  \ \  \___|\ \  \___|\ \  \|\  \ 
              \ \   ____\ \_____  \ \  \    \ \   ____
               \ \  \___|\|____|\  \ \  \____\ \  \___|
                \ \__\     ____\_\  \ \_______\ \__\   
                 \|__|    |\_________\|_______|\|__|   
                          \|_________|                 
          """                                                               

print(message)

while True:
    command = input(">>> ")

    if command=="exit":
        sys.exit()

    else:
        com = Command()
        dicts = com.command_start(command)
        sc = select_choice(dicts)
        if dicts["action"] is "get" or dicts["action"] is "put":
            passd = input("password")
            sc.get_put_fetch(passd)
        else:
            sc.other()
            


