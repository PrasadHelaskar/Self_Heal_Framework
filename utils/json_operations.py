import json

class json_operations():
    def __init__(self,filename=None):
        self.filename= filename
        self.__private_file_path=f"/mnt/k/self_heal_framework/code/locators/{self.filename}.json"

    def json_read(self):
        """
            For reading the json file
        """
        with open(self.__private_file_path, 'r',encoding='uft-8') as json_file:
            data=json.load(json_file)

            return data

    def json_read_key(self,key):
        """
            For reading the json file and fetch a value for specific key
        """
        with open(self.__private_file_path, 'r',encoding='uft-8') as json_file:
            data=json.load(json_file)

            return data[key]

    def json_write(self,key,value):
        """
            For updaing the json file
        """
        with open(self.__private_file_path,'r',encoding='uft-8') as json_file:
            data=json.load(json_file)

            data[key]=value

        with open(self.__private_file_path,'w',encoding='uft-8') as json_file:
            json.dump(data,json_file,indent=4)