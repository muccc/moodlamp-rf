#!/usr/bin/python

clock = 16000000
basefreq = 125
levels = 256
interval_cycles = 64000

if __name__ == "__main__":
    last = 0
    sum = 0
    for i in range(1,levels):
        cycles = (i/float(levels-1))**2*float(clock)/float(basefreq)
        delta = round(cycles-last)
        print round(cycles)
        last = cycles
        sum+=delta

