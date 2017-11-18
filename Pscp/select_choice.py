from ssh_connect import SSh_Connect
from storage_data import Storage_Data
class Select_Choice():

    def __init__(self,dict_type):
        self.dict_type = dict_type
        self.ssh_con = SSh_Connect()
        self.sd = Storage_Data()

    def get_put_fetch(self,password):
        users = self.dict_type["user"]
        host  = self.dict_type["hostname"]
        self.ssh_con.connect(host,user,password)
        # get or put
        if self.dict_type["action"] is "get":
            # if dirs
            if "r" in self.dict_type.keys() is True:
                self.ssh_con.get_dir(self.dict_type["from"],self.dict_type["to"])
                # get file
            else:
                self.ssh_con.get(self.dict_type["from"],self.dict_type["to"])

        elif self.dict_type["action"] is "put":
            # if dirs
            if "r" in self.dict_type.keys() is True:
                self.ssh_con.put_dir(self.dict_type["from"],self.dict_type["to"])
            else:
                # put file
                self.ssh_con.put(self.dict_type["from"],self.dict_type["to"])

        else:
            pass




    def shows(self):
        show_data = self.sd.show_database()
        # 登録情報を表示
        for user,hostname,Keywords in show_data:
            print("Keywords: {keysd}".format(keysd=Keywords))
            print("USER     ---> {users}".format(users=user))
            print("Host_name---> {host}".format(host=hostname))
            print("\n")

    def register(self):
        print("Please input your username")
        username = input("USER: ")
        print("Please input your hostname")
        hostname = input("HOST_NAME: ")
        print("Please input your keyword")
        keywords = input("KEYWORDS:" )
        self.sd.insert_database(username,hostname,keywords)
        print("Register log")
        
        
