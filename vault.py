import os


def GetBinList(dir):
    bins = [f for f in os.listdir(dir) if f[-4:] == ".bin"]
    return [os.path.join(dir, f) for f in bins]

bins = GetBinList(os.getcwd())


for fi in bins:
    i = 0
    print("opening", fi)
    fa = open(fi, "rb")
    bet = fa.read(3)
    a = bet.hex()
    b = 'ffd8ff'
    res = int(a, 16) ^ int(b, 16)
    res = hex(res)
    res = res[:4]
    print("xor byte is", res)
    res = int(res, 16)
    new = open(fi+".jpg", "wb")
    barr = []
    print("decrypting file......")
    with open(fi, "rb") as f:
        byte = f.read(1)
        while byte:
            if i < 128:
                bytem = int(byte.hex(), 16) ^ res
                barr.append(bytem)
            else:
                barr.append(int(byte.hex(), 16))
            i = i+1
            byte = f.read(1)
    #print(barr)
    barrb = bytes(barr)
    new.write(barrb)
    new.close()
    fa.close()
    print("SUCCESS!")
