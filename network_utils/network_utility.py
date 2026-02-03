from utils.logger import Logger

log=Logger().get_logger(__name__)

class ApiListner():

    def __init__(self,driver):
        self.driver=driver
        self.api_list = [
            "saucedemo"
        ]

    def _response_fromatter(self,request) -> dict:
        response_time=None

        if request.date and request.response and request.response.date:
            response_time= round((request.response.date-request.date).total_seconds()* 1000, 2)

        return({
            "url": request.url,
            "method": request.method,
            "status": request.response.status_code,
            "time": response_time
        })

    def api_analysis(self,api_list=None,print_log=False,capture_all=False) -> list:
        responces=[]

        for request in self.driver.requests:
            if not request.response:
                continue

            if capture_all:
                for api in request.url:
                    responces.append(self._response_fromatter(request))

            else:
                if not api_list:
                    api_list=self.api_list

                for api in api_list:
                    if api in request.url:
                        responces.append(self._response_fromatter(request))

        if not responces:
            raise AssertionError("No matching API are found during execution")

        if print_log:
            for api_call in responces:
                log.info(api_call)

        return responces