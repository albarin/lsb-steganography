import os, sys
import Image
import functions

image_path = sys.argv[1]

image = Image.open(image_path)
image_width, image_height = image.size
image_pixels = image.load()

bits = []
for i in range(image_height):
    for j in range(image_width):
        r = image_pixels[j,i][0]
        g = image_pixels[j,i][1]
        b = image_pixels[j,i][2]
        
        bits += [functions.getBit(r, 0)]
        bits += [functions.getBit(g, 0)]
        bits += [functions.getBit(b, 0)]

i = 0
byte = 0
hidden_bytes = []
for p in range(len(bits)):
    if i == 8:        
        hidden_bytes += [byte]
        i = 0
        byte = 0
    byte = functions.changeBit(byte, bits[p], 7-i)
    i += 1

width = hidden_bytes.pop(0)
height = hidden_bytes.pop(0)
p = 0
i = 0
j = 0
end = False
list_of_pixels = [0 for x in range(width*height)]
while i < width and not end:
    j = 0
    while j < height and not end:
        r = hidden_bytes.pop(0)
        g = hidden_bytes.pop(0)
        b = hidden_bytes.pop(0)
        list_of_pixels[i+j*width] = (r,g,b)

        if len(hidden_bytes) < 3:
            print len(hidden_bytes)
            end = True
        
        j += 1
    i += 1

im = Image.new(image.mode, (width, height))
im.putdata(list_of_pixels)
im.save("decoded.png")
