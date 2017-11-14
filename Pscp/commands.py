

"""
get -c pi@10.1.121.24 -from remote -to local

get -n rasp -from remote -to local

put -c pi@10.1.121.24 -from remote -to local

put -n rasp -from remote -to local

regester --> register user and IP

show --> IP shows 
"""

class Command():
    def __init__(self):
        self.command_dict = {}

    def action_type(self):
        if self.command_dict["action"]=="get" or self.command_dict["action"]=="put":
             form_true="from" in self.command_dict.keys()  
             to_true="to" in self.command_dict.keys()
             if form_true is True and to_true is True:
                return self.command_dict
             else:
                return "argment is not -from or -to"
        else:
            return self.command_dict

    def command(self,options):
        if len(options)==1:
            self.command_dict[options[0]] = options[0]

        else:
            self.command_dict[options[0]] = options[1]

    def command_start(self,data):
        spl_data = data.split("-")
        for number,options in enumerate(spl_data):
            datas = options.strip()
            data_list = datas.split(" ")
            if number==0:
                self.command_dict["action"] = data_list[0]
            else:
                self.command(data_list)

        command = self.action_type()
        return command

if __name__ == "__main__":
    command = Command()
    data = "get -r -c pi@10.21.4.5 -from /user/test -to /tst/ed"
    command.command_start(data)
