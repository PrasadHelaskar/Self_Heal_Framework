from utils.json_operations import json_operations
from utils.logger import Logger

log=Logger().get_logger(__name__)

class SmartLocators():

    def __init__(self,page_name:str=None):
        self.page_name=page_name.lower()
        self.json_op=json_operations(page_name)

        self.data=self.json_op.json_read()

    def get_locators_by_element_name(self,element_name):
        """
            get_locators_by_element_name used to fetch the all locators in the json file related to the param called element_name
            
            param element_name: this is the element which we are fetching the and passsing it to the selenium methods tp perfore action  
        """
        if element_name not in self.data:
            raise KeyError(f"{element_name} not present on {self.page_name} page or misspelled")
        
        locator=self.data[element_name]

        return{
            "primary": locator.get("primary"),
            "fallback": locator.get("fallback", [])
        }

    def convert_locator_to_list(self, element_name):
        """
            convert_locator_to_list revicing the dict from get_locators_by_element_name and convert them to list 
            
            param element_name: this is the element which we are fetching the and passsing it to the selenium methods tp perfore action
        """
        data=self.get_locators_by_element_name(element_name)

        return [data["primary"]]+data["fallback"]
    
    def update_primary_locator(self,element_name,new_locator):
        """
        update_primary_locator is part of healing the locators in json file 
        
        :param element_name:used to decide which element need to be healed 
        :param new_locator: Description
        """

        data=self.get_locators_by_element_name(element_name)

        old_primary=data["primary"]
        fall_back=data["fallback"]

        # removing the new_locator from fallbacks
        new_fallback=[]
        for fb in fall_back:    
            if fb !=new_locator:
                new_fallback.append(fb)

        fall_back=new_fallback

        log.info("Fallback locators are updated")


        # adding old_locatoe to fallbacks
        if old_primary not in fall_back:
            fall_back.insert(0,old_primary)

        updated_data={
            "primary":new_locator,
            "fallback":fall_back
        }

        self.json_op.json_write(element_name, updated_data)

        log.info(f"the {element_name} locators are healed")