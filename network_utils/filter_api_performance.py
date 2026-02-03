from network_utils.network_utility import ApiListner

def performance_filter(driver):
    performance_list=ApiListner(driver).api_analysis(capture_all=True)
    api_timings=[]

    for api in performance_list:
        api_timings.append(api["time"])
    
    api_timings.sort()

    slowest=api_timings[-1]
    fastest=api_timings[1]

    avg_time=sum(api_timings)/len(api_timings)

    return ([slowest,fastest,avg_time])