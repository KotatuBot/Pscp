import sys
from select_choice import select_Choice
from command import Command
from getpass import getpass

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
    commands = input(">>> ")

    if commands=="exit":
        sys.exit()

    else:
        command = Command()
        # optionのディクトを作成する
        dicts = command.command_start(commands)
        if dicts["action"] is "get" or dicts["action"] is "put":
            password = getpass("Password: ")
            # それぞれの処理を行う
            sc = select_choice(dicts)
            sc.get_put_fetch(password)
        elif dicts["action"] is "show":
            sc.shows()

        elif dicts["action"] is "register":
            keywords = command.split(" ")[1]
            sc.register(keywords)
        else:
           pass 
            


