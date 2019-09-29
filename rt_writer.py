import numpy as np
import h5py

class RTWrites():

    def __init__(self):
        #self.x = 6250000
        self.x = 50000
        self.y = 5
        self.z = 1000


    def Writer(self):
        hf = h5py.File('data.h5', 'w')
        self.d1 = np.random.random(size=(self.x, self.y))


        for i in range(self.z):
            hstra = 'dataset_' + str(i) + "_a"
            hstrb = 'dataset_' + str(i) + "_b"
            hgrp = 'group_' + str(i)
            g2 = hf.create_group(hgrp)
            g2.create_dataset(hstra, data=self.d1)
            g2.create_dataset(hstrb, data=self.d1)

        print("Data Set Written")
        hf.close()


