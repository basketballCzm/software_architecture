#!/usr/bin/python
import websocket
import _thread
import time
from threadpool import ThreadPool, makeRequests
import json
from get_machine_info import MachineStatus
import random

def on_message(ws, message):
    pass

def on_error(ws, error):
    pass

def on_close(ws):
    print ("### closed ###")

def on_open(ws):
    id = random.randint(1000000,9999999);
    for x in range(1,10):
        time.sleep(1)
        MS = MachineStatus()
        #print (MS.IP, '\n', MS.MAC, '\n', MS.cpu, '\n', MS.mem, '\n', MS.status)
        machine_data = {
        "ID":id,
        "IP":MS.IP,
        "MAC":MS.MAC,
        "CPU":MS.cpu,
        "MEM":MS.mem,
        "STATUS":MS.status
        }
        ws.send(json.dumps(machine_data))
    time.sleep(1)
    ws.close()
    print ("thread terminating...")

def on_start(a):
    time.sleep(a%20)
    #websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://127.0.0.1:8000",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open

    ws.run_forever()

if __name__ == "__main__":
    pool = ThreadPool(5)
    test = list()
    for ir in range(5):
        test.append(ir)
    requests = makeRequests(on_start, test)
    [pool.putRequest(req) for req in requests]
    pool.wait()
