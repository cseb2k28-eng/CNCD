def crc(data, poly, bits):
    data = data << bits
    while data.bit_length() >= poly.bit_length():
        data ^= poly << (data.bit_length() - poly.bit_length())
    return data

s = input("Enter data: ")

data = int.from_bytes(s.encode(), "big")

crc12 = crc(data, 0x180F, 12)
crc16 = crc(data, 0x11021, 16)
crc_ccitt = crc(data, 0x11021, 16)

print("CRC-12:", format(crc12, "03X"))
print("CRC-16:", format(crc16, "04X"))
print("CRC-CCITT:", format(crc_ccitt, "04X"))