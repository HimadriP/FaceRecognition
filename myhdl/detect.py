from myhdl import *
from brightness_increement import *
from  median_filter import *
from skin_threshold import *
from contrast_correction import *
#from rgb_to_ycbcr import *

def clkDriver(clk):
    halfPeriod = delay(10)
    @always(halfPeriod)

    def driverclk():
        clk.next = not clk

    return driverclk

clk = Signal(0)
clkin = clkDriver(clk)

r=Signal(intbv(30))
g=Signal(intbv(60))
b=Signal(intbv(90))
br=Signal(intbv(25))

oro=Signal(intbv(30))
ob=Signal(intbv(30))
og=Signal(intbv(30))
ora=Signal(intbv(30))
oba=Signal(intbv(30))
oga=Signal(intbv(30))

a = brightness_increement(r,g,b,br,clk,oro,ob,og)
#b = contrast_correction(oro,og,ob,clk,ora,oga,oba)

def channel_in(clk):
    channel = [[None for i in range(20)] for j in range(20)]
    for i in range(20):
        for j in range(20):
            channel[i][j] = brightness_increement(r,g,b,br,clk,oro,ob,og)
            
    return instances()

cin = channel_in(clk)
sim = Simulation(clkin,cin)
sim.run(100)