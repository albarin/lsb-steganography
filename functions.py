def changeBit(byte, bit, position):
	if bit == 1:
		byte |= 1 << position
	else:
		byte &= ~(1 << position)

	return byte

def getBit(byte, position):
	mask = 1 << position
	result = byte & mask

	return result >> position

def getBits(byte):
	bits = []
	for i in range(7, -1, -1):
		bits.append(getBit(byte, i))
	
	return bits
