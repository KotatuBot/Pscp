from ssh_connect import SSh_Connect
class select_Choice():

    def __init__(self,dict_type):
        self.dict_type = dict_type
        self.ssh_con = SSh_Connect()

    def get_put_fetch(self,passwd):
        # get user and IP
        # get database
        if "n" in self.dict_type.keys() is True:
            pass
        elif "c" in self.dict_type.keys() is True:
            user_IP = dict_type["c"].split("@")
            user = user_IP[0]
            host = user_IP[1]
        else:
            print("This is not input IP and Host")

        # connect
        self.ssh_con.connect(host,user,passwd)
        # get or put
        if self.dict_type["action"] is "get":
            # if dirs
            if "r" in self.dict_type.keys() is True:
                self.ssh_con.get_dir(self.dict_type["from"],self.dict_type["to"])
            else:
                # get file

        elif self.dict_type["action"] is "put":
            # if dirs
            if "r" in self.dict_type.keys() is True:
                self.ssh_con.put_dir(self.dict_type["from"],self.dict_type["to"])
            else:
                # get file




    def other(self):
        # show
        if self.dict_type["action"] is "show":
            pass
        # register
        else:
            pass
        
        
