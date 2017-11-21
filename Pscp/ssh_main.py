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
                from_string = dicts["from"]
                to_string = dicts["to"]
                if from_string == "from" or to_string == "to":
                    print("Path is not set for --from or --to")
                elif from_string == "" or to_string=="":
                    print("There is too much space between --from or --to and the path.")
                    print("Please leave one blank space")
                else:
                    password = getpass("Password: ")
                    # それぞれの処理を行う
                    sc.get_put_fetch(password)
        elif dicts["action"]=="show":
            sc.shows()
        elif dicts["action"]=="register":
            sc.register()
        else:
           print("Icorrect argument or command ")
