class SSh_Help():
    def __init__(self):
        pass

    def help_show(self):
        message = """
        usage:\n
             [action] [-r] [-c user@hostname] [-n Keywords] [-from Source_path] [-to Destination_path]\n
        [action]: \n
                 You can specify the following actions\n
                 get: Retrieve files from remote
                 put: Upload files remotely
                 register: Add an alias to omit the user name and host name.
                           Can be used with later -n command
                 show: Display all registered aliases
                 help: You can display the commands you can use
                 exit: You can quit Pscp

         [option]:\n
                 
                 -r: Recursively perform copy operations (copy in directory)
                 -c: Specify user name and host name (specified by user @ hostname)
                 -n: Use registered alias
                 -from: Specify directory path or file path of copy source
                 -to: Specify directory path or file path of copy destination

         [example]:\n
                 get -c mikan@10.1.13.45 -from /home/TEST/test.txt -to /home/mikan
                     --> Copy test.txt to the mikan user's /home/mikan directory\n
                 get -n rasp -from /home/TEST/test.txt -to /home/mikan
                     --> Copy test.txt to the mikan user's /home/mikan directory using alias rasp\n
                 get -r -c mikan@10.1.13.45 -from /home/kotatu/TEST2 -to /home/mikan
                    --> Copy the TEST 2 directory to the mikan user's /home/mikan directory\n
                 put -c mikan@10.1.13.45 -from /home/mikan/test.txt -to /home/TEST
                    --> Upload test.txt in mikan user's /home/mikan directory to /home/TEST\n
                 put -r -c mikan@10.1.13.45 -from /home/mikan/TEST2 -to /home/TEST
                    --> Upload the TEST 2 directory of mikan user's /home/mikan to /home/TEST\n
                 register
                    --> Register alias\n
                 show
                    --> Display all registered items\n
                  
                  """
        print(message)
