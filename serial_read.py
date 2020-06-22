from serial import Serial
import time

NO_NODES = 15
nodes_data = {k: {} for k in range(1, NO_NODES+1) }

ser = Serial('/dev/pts/1', 9600, timeout=1)
while True:
    reading = str(ser.readline())
    try:
        _readings = reading.rstrip().split(',')
        _id  = int(_readings[0].split("I:")[1])
        temp = float(_readings[1].split("T:")[1])
        node = int(_readings[2].split("N:")[1].replace("\\n'", ""))

        print("_id", _id, "temp", temp, "node", node)
        nodes_data[node][_id] = temp

        for _nID, _node in nodes_data.items():
            lists = sorted(_node.items()) # sorted by key, return a list of tuples
            x, y = zip(*lists) # unpack a list of pairs into two tuples

            print(_nID, lists)
            


    except Exception as e:
        print(e)
        pass