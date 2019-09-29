import tiller.rt_writer as t
import tiller.rt_reader as r

class Main():

    def __init__(self):
        self.rtw = t.RTWrites()


    def run(self):
        self.rtw.Writer()
        self.rtr1 = r.RTReader()
        self.rtr2 = r.RTReader()
        self.rtr3 = r.RTReader()
        self.rtr4 = r.RTReader()
        self.rtr5 = r.RTReader()
        self.rtr1.start()
        self.rtr2.start()
        self.rtr3.start()
        self.rtr4.start()
        self.rtr5.start()




m = Main()
m.run()