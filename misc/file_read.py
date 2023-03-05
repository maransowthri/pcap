
with open('./sample.txt') as f:
    # Read first 10 charecters
    # print(f.read(10))
    # print(f.read(10))
    # Updating the file stream pointer to starting point
    # f.seek(0)
    # print(f.readline())
    # f.seek(0)
    # print(f.readlines(2))
    for line in f:
        print(line)
