class select_Choice():

    def __init__(self,dict_type):
        self.dict_type = dict_type

    def get_put_fetch(self,passd):
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

    def other(self):
        # show
        if self.dict_type["action"] is "show":
            pass
        # register
        else:
            pass
        
        
