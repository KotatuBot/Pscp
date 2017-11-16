import sys
from select_choice import select_Choice
from command import Command

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
        elif dicts["action"] is "show":
            sc.shows()

        elif dicts["action"] is "register":
            keywords = command.split(" ")[1]
            sc.register(keywords)
        else:
           pass 
            


