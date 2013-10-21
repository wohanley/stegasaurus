'''
Created on Sep 12, 2011

@author: Willy
'''

import png
import sys

filename = sys.argv[1]

# Get the image data
if filename[-3:].lower() == "png":
    picture = png.Reader(filename)
    
imageData = picture.read_flat()
pixels = imageData[2]

message = ""
currentChar = ord(' ')
charCount = 0

while currentChar != ord('\0'):
    binString = ""
    for i in xrange(0, 8):
        if pixels[charCount * 8 + i] % 2 == 0:
            binString += '0'
        else:
            binString += '1'
    currentChar = int(binString, 2)
    message += chr(currentChar)
    charCount += 1
    
print message
