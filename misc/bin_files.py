data = bytearray(100)

# Can only hold data upto 255
data[0] = 100
data[1] = 120

# wb means write binary
with open('sample.bin', 'wb') as f:
    f.write(data)

# rb means read binary
with open('sample.bin', 'rb') as f:
    for byte in f.read():
        print(int(byte), end=' ')