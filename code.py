import psutil
import datetime
import requests

def getVirtualMemValue():
    virtual_mem = psutil.virtual_memory()
    return virtual_mem.percent
    

def getCPUValue():
    cpu = psutil.cpu_percent(0.1)
    return cpu


def getDisksValue():
    disks = psutil.disk_usage('/')
    return disks.percent



def main():

    mem_val = getVirtualMemValue()
    cpu_val = getCPUValue()
    disks_val = getDisksValue()
    measure_time = datetime.datetime.now()


    values = {'mem_val': mem_val, 'cpu_val': cpu_val, 'disks_val': disks_val}
    params = {'measure_time': measure_time}

    requests.post('http://localhost:8000/api/sensor-history/', data=values, params=params)

if __name__ == '__main__':
    main()