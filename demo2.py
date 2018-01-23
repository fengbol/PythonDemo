#字符串编码

#获取字符整数表示
ord("A")
ord("中")
#把编码转换为对应字符
chr(66)
chr(25991)

#还可以用十六进制表示
print("\u4e2d\u6587")

#字节bytes需要用b前缀
x = b"ABC"
#encode()方法可以把字符串编码为指定bytes
"ABC".encode("ascii")
"中文".encode("utf-8")#注意ascii不能编码中文
#decode()方法用于解码
x.decode("ascii")
b"\xe4\xb8\xad\xe6\x96\x87".decode("utf-8")
#加入ignore可以忽略不能解码的字节
b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')

#len()方法可以获取字符串长度，如果换成bytes就计算字节数
len(x)
len(b'ABC')                       #3 英文只占一个字节
len("中文".encode("gbk"))         #4 gbk/gb2312之类中文占两个字节
len(b'\xe4\xb8\xad\xe6\x96\x87')
len('中文'.encode('utf-8'))       #6 utf-8/unicode等中文占三个字节
#Python默认使用Unicode，转换尽量也使用Unicode

#格式化字符串,%s表示用字符串替换，%d表示用整数替换，%f是浮点数，%x是十六进制整数，占位符顺序不能变
print("Age:%d,Gender:%s" %(25,True))
print('%.3f' % 3.1415926)           #3.142
#可以用%%表示“%”字符串
#format()方法有点类似C#里的string.format方法
"Hello,{0},I'm {1:.2f}?".format("bill",3.14159)
