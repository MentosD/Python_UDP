## client code
# 导入所需的库
import socket
import datetime
import struct
import time
​
# 配置UDP
BUFSIZE = 32  # 缓冲池容量
ip_serverport = ('192.168.8.119', 8123)  # Server端ip地址及端口
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 无需更改
​
print('开始UDP通讯_Client端')
for i in range(1, 10):
    a = i  # 发送内容 i （浮点数格式）
    msg = struct.pack("d", a)  # 数据打包
    time.sleep(1)  # 间隔一秒
    client.sendto(msg, ip_serverport)  # 发送至Server
    print('向Server端发送了', a)
