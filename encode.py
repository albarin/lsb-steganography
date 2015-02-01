import os, sys
import Image
import functions

cover_path = sys.argv[1]
message_path = sys.argv[2]

cover = Image.open(cover_path)
cover_width, cover_height = cover.size
cover_total = cover_width * cover_height

message = Image.open(message_path)
message_width, message_height = message.size
message_total = message_width * message_height

# cada pixel puede guardar 3 bits
max_bits = cover_total * 3
# cada pixel se compone de 24 bits y se necesitan 2 bytes extra para guardar width y height
message_bits = (message_total * 24) + 16

if message_bits > max_bits:
    print "Message too long"
    sys.exit(0)

message_list = []
message_list += functions.getBits(message_width)
message_list += functions.getBits(message_height)
message_pixels = message.load()
for i in range(message_width):
    for j in range(message_height):
        r = message_pixels[i, j][0]
        g = message_pixels[i, j][1]
        b = message_pixels[i, j][2]
        
        message_list += functions.getBits(r)
        message_list += functions.getBits(g)
        message_list += functions.getBits(b)
    
p = 0
list_of_pixels = []
cover_pixels = cover.load()
for i in range(cover_height):    
    for j in range(cover_width):
        r = cover_pixels[j,i][0]
        g = cover_pixels[j,i][1]
        b = cover_pixels[j,i][2]
        
        if p < len(message_list):
            bit = message_list[p]
            r = functions.changeBit(r, bit, 0)
            p += 1
            
        if p < len(message_list):
            bit = message_list[p]
            g = functions.changeBit(g, bit, 0)
            p += 1
            
        if p < len(message_list):
            bit = message_list[p]
            b = functions.changeBit(b, bit, 0)
            p += 1
        list_of_pixels.append((r,g,b))

im2 = Image.new(cover.mode, cover.size)
im2.putdata(list_of_pixels)
im2.save("encoded.png")