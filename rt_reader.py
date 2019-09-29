import h5py
import io
import numpy as np
import datetime as dt
import threading

class RTReader(threading.Thread):

    def __init__(self):
        self.x = 50000
        self.y = 5
        self.z = 1000
        self.data = h5py.File('data.h5', 'r')
        threading.Thread.__init__(self)

    def getGroup(self,group):
        for dset in self.data[group]:
            g1 = np.array(self.data[group].get(dset))
            # print(g1)

    def run(self):

        start = dt.datetime.today().timestamp()
        tfkey = self.data.keys()
        #print("Keys: %s" % tfkey)
        for group in self.data.keys():
            self.getGroup(group)

        stop = dt.datetime.today().timestamp()
        elapsed = stop - start
        persec = self.z / elapsed
        print("Wrapped in {} seconds".format(elapsed))
        print("Equal to {} per second".format(persec))


        print("Done Reading")
        self.data.close()

