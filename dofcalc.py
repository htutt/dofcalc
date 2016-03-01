# Depth of Field calulation
# pk.htut@gmail.com
# copyright 2016 @ Phone Kyaw Htut
# March 2st, 2016


def hyperfocal(focallength, aperture, coc):
    "Calculating Hyperfocal"    
    hyfocal = (focallength * focallength)/(aperture*coc)
    return (hyfocal)

def dof(h, d, l):
    "Calculating Depth of Field"
    # h = hyperfocal, d = distance, l = focal length
    nearpoint = (h * d)/(h + (d - l))
    farpoint = (h * d)/(h - (d - l))
    totaldof = farpoint - nearpoint
    return (nearpoint, farpoint, totaldof)

def CoC():
    "Determining Circle fo Confusion"
    sensor_size = raw_input("Camera sensor: 1. Full frame, 2. Crop frame? ")
    s = int(sensor_size)
    if s == 1:
        C = 0.02501 # CoC for full frame
    elif s == 2:
        C = 0.019948 # CoC for crop frame
    else:
        print "Please enter 1 or 2"
    return (C)

focal = raw_input("Enter focal length (mm): ")
L = int(focal)

fstop = raw_input("Enter aperture value: ")
A = float(fstop)

dist = raw_input("Enter distance to subject (feet): ")
D = float(dist) / 0.00328084 # Change ft to mm

H = hyperfocal(L, A, CoC()) # Get value in mm

DF = dof(H, D, L) # Get value in mm

# Print in feet
print "\n=====Depth-Of-Field Results======"
print "Near point of DOF: %.2f ft " % (DF[0]*0.00328084)
print "Far point of DOF: %.2f ft" % (DF[1]*0.00328084)
print "Total DOF: %.2f ft" % (DF[2]*0.00328084)
print "Hyperfocal distance: %.2f ft" % (H*0.00328084)
print "=================================\n"
