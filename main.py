import struct


def demo1():
    # 使用bin_buf = struct.pack(fmt, buf)将buf为二进制数组bin_buf
    # 使用buf = struct.unpack(fmt, bin_buf)将bin_buf二进制数组反转换回buf

    # 整型数 -> 二进制流
    buf1 = -256
    bin_buf1 = struct.pack('>i', buf1) # 'i'代表'integer'
    ret1 = struct.unpack('>i', bin_buf1)
    print(bin_buf1, '  <====>  ', ret1)

    # 浮点数 -> 二进制流
    buf2 = 6.013470016999068e-154
    bin_buf2 = struct.pack('1d', buf2) # 'd'代表'double'
    ret2 = struct.unpack('1d', bin_buf2)
    print(bin_buf2, '  <====>  ', ret2)

    # 字符串 -> 二进制流
    buf3 = 'Hello World'
    bin_buf3 = struct.pack('11s', buf3.encode("utf-8")) # '11s'代表长度为11的'string'字符数组
    ret3 = struct.unpack('11s', bin_buf3)
    print(bin_buf3, '  <====>  ', ret3)

    # 结构体 -> 二进制流
    # 假设有一个结构体
    # struct header {
    #   int buf1;
    #   double buf2;
    #   char buf3[11];
    # }
    bin_buf_all = struct.pack('id11s', buf1, buf2, buf3.encode("utf-8"))
    ret_all = struct.unpack('id11s', bin_buf_all)
    print(bin_buf_all, '  <====>  ', ret_all)


if __name__ == "__main__":
    demo1()
    bin(1)
    int