import psutil
import datetime
import urllib.request
import urllib.parse
import json

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

    values = {'mem_val': mem_val, 'cpu_val': cpu_val, 'disks_val': disks_val}

    for each in values:

        values_item = {'slug': each, 'value': values[each]}
        json_data = json.dumps(values_item)
        json_data = json_data.encode('ascii')
        req = urllib.request.Request('http://localhost:8000/api/sensor-history/')
        req.add_header('Content-Type', 'application/json')

        response = urllib.request.urlopen(req, json_data)

    


    


if __name__ == '__main__':
    main()