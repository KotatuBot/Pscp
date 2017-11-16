import sqlite3

class Storage_Data():
    def __init__(self):
        self.database_name = ""
        self.database_table = ""

    def create_data(self):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        create_table = '''create table {database_table} ( user varchar(64), 
                                               ip varchar(64),
                                               keys varchar(64) 
                                              )'''.format(database_table = self.database_table)
        c.execute(create_table)
        conn.close()

    def insert_database(self,user,ip,keywards):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        sql = "insert into {database_table} (user,ip,keys) values (?,?,?)".format(database_table=self.database_table)
        insert_data = [user,ip,keywards]
        c.execute(sql,insert_data)
        conn.commit()
        conn.close()


    def fetch_database(self,keywords):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        select_sql = "select * from {database_table} where keys=?".format(database_table=self.database_table)
        for row in c.execute(select_sql,[keywords]):
            print(row)

