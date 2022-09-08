import sqlite3


class HandleDB(): #nos ayudara a controlar la base de datos, obtener stats e insertar registros si no existen
    def __init__(self):
        self._con = sqlite3.connect("./database.db")
        self._cur = self._con.cursor()
        
    def get_stats(self, data_record):
        data = self._cur.execute("SELECT  COUNT(id)  as 'count',(select COUNT(id)from records) as 'total' from records where result ='{}'".format(data_record))
        return data.fetchone()
    
    def insert(self, data_record):
        self._cur.execute("INSERT OR IGNORE INTO records (array,result) VALUES('{}',{})".format(
            data_record["array"],
            data_record["result"]
        ))
        self._con.commit()    
            
    def __del__(self):
        self._con.close()
    
