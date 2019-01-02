import struct

def binary(i: int) -> int:
    r = str(i%2)
    s = int(i/2)
    while s >= 1:
        r = r + str(s)
        s = s/2
    r = list(r)
    r.reverse()
    return bytes(("0b" + "".join(r)).encode("ascii"))


def int_from_binary_str(bin_string: str) -> int:
    return int(bin_string, base=2)

def int_3_byte():
    pass


def four2three():
    f = b"\x00\x3f\x3f\x3f\x00\x3f\x3f\x3f\x00\x3f\x3f\x3f\x00\x3f\x3f\x3f"
    struct.unpack("I", b"\x00\x3f\x3f\x3f")
    remainder = len(f) % 4
    if remainder is not 0:
        raise ValueError
    t = b""
    for i in range(int(len(f) / 4)):
        t = t + f[4*i: 4*i + 4][1:]
    print(t)
    byte_nums = [str("0000000" + bin(i)[2:])[-8:] for i in list(t)]
    print(int_from_binary_str("0b" + "".join(byte_nums[0:3])))



    pass


if __name__ == "__main__":
    # ss = binary(2)
    # print(binary(2)[0])
    # print(int_from_binary_str("0b10"))
    four2three()
    i = 2