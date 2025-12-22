import os
import json
from dotenv import load_dotenv 

load_dotenv(".config/.env")
class json_operations():
    def __init__(self,filename=None):
        self.filename= filename
        self.__private_file_path=os.getenv("LOCATOR_BASE_PATH")+f"{self.filename}.json"

    def json_read(self):
        """
            For reading the json file
        """
        with open(self.__private_file_path, 'r',encoding='utf-8') as json_file:
            data=json.load(json_file)

            return data

    def json_read_key(self,key):
        """
            For reading the json file and fetch a value for specific key
        """
        with open(self.__private_file_path, 'r',encoding='utf-8') as json_file:
            data=json.load(json_file)

            return data[key]

    def json_write(self,key,value):
        """
            For updaing the json file
        """
        with open(self.__private_file_path,'r',encoding='utf-8') as json_file:
            data=json.load(json_file)

            data[key]=value

        with open(self.__private_file_path,'w',encoding='utf-8') as json_file:
            json.dump(data,json_file,indent=4)