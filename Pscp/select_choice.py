from ssh_connect import SSh_Connect
from storage_data import Storage_Data
class select_Choice():

    def __init__(self,dict_type):
        self.dict_type = dict_type
        self.ssh_con = SSh_Connect()
        self.sd = Storage_Data()

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
                pass

        elif self.dict_type["action"] is "put":
            # if dirs
            if "r" in self.dict_type.keys() is True:
                self.ssh_con.put_dir(self.dict_type["from"],self.dict_type["to"])
            else:
                # get file
                pass

        else:
            pass




    def shows(self):
        show_data = self.sd.show_database()
        # 登録情報を表示
        for data in show_data:
            print(data)

    def register(self,keywords=""):
        self.sd.fetch_database(keywords)
        print("Register log")
        
        
