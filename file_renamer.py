import os, glob, re
from os import listdir
from os.path import isfile, join

#Get the full path for the directory this python file is in
mypath = os.path.dirname(os.path.abspath(__file__))

#Get a list of only other FILES in the same location (NO directories)
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#Go through each file in the list. If it matches the format, rename the file accordingly
for file in onlyfiles:
    result = re.search(r"([A-Za-z]+)\.USUSD_Candlestick_1_s_(ASK|BID)\_(\d{2})\.(\d{2})\.(\d{4})\-\d{2}\.\d{2}\.\d{4}\.csv", file)
    if result != None:
        new_filename = result.group(1) + "_" + result.group(4) + result.group(3) + result.group(5) + "_" + result.group(2)
        print(new_filename)
        os.rename(file, new_filename)