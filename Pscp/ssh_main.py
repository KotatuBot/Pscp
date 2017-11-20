import sys
from select_choice import Select_Choice
from commands import Command
from getpass import getpass
from ssh_help import SSh_Help


message1 = "You can check arguments with the help"
message  = """  
              ________  ________  ________  ________
             |\   __  \|\   ____\|\   ____\|\   __  \  
             \ \  \|\  \ \  \___|\ \  \___|\ \  \|\  \ 
              \ \   ____\ \_____  \ \  \    \ \   ____
               \ \  \___|\|____|\  \ \  \____\ \  \___|
                \ \__\     ____\_\  \ \_______\ \__\   
                 \|__|    |\_________\|_______|\|__|   
                          \|_________|                 
          """                                                               

print(message1)
print(message)

while True:
    commands = input(">>> ")

    if commands=="exit":
        sys.exit()
    elif commands == "help":
        shelp = SSh_Help()
        shelp.help_show()
    else:
        command = Command()
        # optionのディクトを作成する
        dicts = command.command_start(commands)
        sc = Select_Choice(dicts)
        if dicts["action"]=="get" or dicts["action"]=="put":
                password = getpass("Password: ")
                # それぞれの処理を行う
                sc.get_put_fetch(password)
        elif dicts["action"]=="show":
            sc.shows()
        elif dicts["action"]=="register":
            sc.register()
        else:
           print("Icorrect argument or command ")
