from model.handle_db import HandleDB

class Record(): #declaramos el modelo RECORD que nos ayudara a crear el registro en nuestra base de datos
    data_record = {}
    
    def __init__(self,data_record):
        self.db = HandleDB()
        self.data_record = data_record
        
    def createRecord(self):
        self.db.insert(self.data_record)
    
    