a = int(input())
buf2max = buf= 0
while a != 0:
    b = int(input())
    if a == b:
        buf = buf + 1
        if buf > buf2max:
            buf2max = buf
        else:
            buf = 0
        a = b
print(buf2max = 1)