'''
Created on Sep 12, 2011

@author: Willy
'''

import png
import sys

message = raw_input("Enter your message:\n") + '\0'
filename = sys.argv[1]
outFilename = sys.argv[2]

# Get the image data
if filename[-3:].lower() == "png":
    picture = png.Reader(filename)
    
imageData = picture.read_flat()
width = imageData[0]
height = imageData[1]
pixels = imageData[2]

# Convert the message to a sequence of ordinal values
chars = []
for ch in message:
    chars.append(ord(ch));

charCount = 0
for ordinal in chars:
    pixelPosition = charCount * 8
    for i in xrange(7, -1, -1):
        if ordinal % 2 == 0:
            pixels[pixelPosition + i] &= 0B11111110
        else:
            pixels[pixelPosition + i] |= 1
        ordinal = ordinal // 2
    charCount += 1
    
outFile = open(outFilename, 'wb')
writer = png.Writer(width, height)
writer.write_array(outFile, pixels)
outFile.close()
