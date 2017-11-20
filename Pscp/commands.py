import re
import os

import Pscp.storage_data as storage

class Command():
    def __init__(self):
        self.command_dict = {}
        self.storage = storage.Storage_Data()
        message = r"~/*"
        self.home_pattern = re.compile(message)

    def user_host(self):
        """
        host name
        """
        if ("c" in self.command_dict.keys()) is True:
            user_host = self.command_dict["c"]
            user_list = user_host.split("@")
            user = user_list[0]
            host = user_list[1]
            information = (user,host)
            return information
        elif ("n" in self.command_dict.keys()) is True:
            keyword = self.command_dict["n"]
            information = self.storage.fetch_database(keyword)
            if len(information)==3:
                user = information[0]
                host = information[1]
                return (user,host)
            else:
                return (False,False)
        else:
            print("argment is not -c or -r")
            return (False,False)

    def home_change(self,keys):
        paths = self.command_dict[keys]
        # home/dir/ is True
        if len(re.findall(self.home_pattern,paths)) == 1:
            file_list = paths.split("~")
            absolute_file = os.environ["HOME"]+file_list[1]
            self.command_dict[keys]=absolute_file


    def action_type(self):
        """
        get action
        """
        if self.command_dict["action"]=="get" or self.command_dict["action"]=="put":
             if ("from" in self.command_dict.keys())is True and ("to" in self.command_dict.keys()) is True:
                 self.home_change("from")
                 self.home_change("to")
                 user,hostname = self.user_host()
                 self.command_dict["user"] = user
                 self.command_dict["hostname"] = hostname
                 return self.command_dict
             else:
                return "argment is not -from or -to"
        else:
            return self.command_dict

    def command(self,options):
        # case only option is one
        if len(options)==1:
            self.command_dict[options[0]] = options[0]
        # case  option is two
        else:
            self.command_dict[options[0]] = options[1]

    def command_start(self,data):
        spl_data = data.split("-")
        # get option dict
        for number,options in enumerate(spl_data):
            datas = options.strip()
            data_list = datas.split(" ")
            # fetch action type
            if number==0:
                self.command_dict["action"] = data_list[0]
            else:
                self.command(data_list)
        # think action type
        command_dict = self.action_type()
        return command_dict

if __name__ == "__main__":
    command = Command()
    data = "get -r -c pi@10.21.4.5 -from /user/test -to /tst/ed"
    a = command.command_start(data)
    print(a)
