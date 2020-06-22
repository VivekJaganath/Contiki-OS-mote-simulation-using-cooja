import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import serial

NO_NODES = 8

#initialize serial port
ser = serial.Serial()
ser.port = '/dev/pts/2' 
ser.baudrate = 9600
ser.timeout = 10
ser.open()

if ser.is_open==True:
	print("\nAll right, serial port now open. Configuration:\n")
	print(ser, "\n") #print serial parameters

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

nodes_data = {k: {} for k in range(1, NO_NODES+1) }

x = []
y = []
# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    reading = str(ser.readline())
    try:
        _readings = reading.rstrip().split(',')

        _id  = int(_readings[0].split("I:")[1])
        temp = float(_readings[1].split("T:")[1])
        node = int(_readings[2].split("N:")[1].replace("\\n'", ""))

        print("_id", _id, "temp", temp, "node", node)

        # plt.plot(x, y)
        # plt.show()

        # Add x and y to lists
        nodes_data[node][_id] = temp
        
        nodes_data[node] = nodes_data[node]

        # Limit x and y lists to 20 items
        #xs = xs[-20:]
        #ys = ys[-20:]

        ax.clear()
        for _nID, _node in nodes_data.items():
            lists = sorted(_node.items())[-5:] # sorted by key, limit to 5
            print(_nID, lists)
            try:
                x, y = zip(*lists) # unpack a list of pairs into two tuples
                ax.plot(x, y, label=_nID)
            except Exception as e:
                pass


        # Draw x and y lists
        # ax.plot(xs, ys, label="Experimental Probability")

        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('Temperature')
        plt.ylabel('Temp (c)')
        plt.legend()
        # plt.axis([1, None, 0, 1.1]) #Use for arbitrary number of trials
        #plt.axis([1, 100, 0, 1.1]) #Use for 100 trial demo

    except Exception as e:
        print(e)
        pass
	

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(x, y), interval=500)
plt.show()