import sqlite3
import os

class Storage_Data():
    def __init__(self):
        home_dir = os.environ["HOME"]
        self.database_name = home_dir +"/"+".alias.db"
        self.database_table = "alias_table"

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
        one_list = ""
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        select_sql = "select * from {database_table} where keys=?".format(database_table=self.database_table)
        for row in c.execute(select_sql,[keywords]):
            one_list = row
        return one_list

    def show_database(self):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        select_sql = "select * from {database_table}".format(database_table=self.database_table)
        show_data = list(c.execute(select_sql))
        c.close()
        return show_data


