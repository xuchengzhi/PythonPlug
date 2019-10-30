import socket
import platform

def get_platform():
    '''''获取操作系统名称及版本号'''
    return platform.platform()

def get_system():
    '''''获取操作系统类型'''
    return platform.system()

def get_ip_addr(ifname):
    #获取本机电脑名
    myname = socket.getfqdn(socket.gethostname(  ))
    #获取本机ip
    if get_system() == "Windows":
        myaddr = socket.gethostbyname(myname)
    else :
        import fcntl
        import struct
          
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        myaddr =  socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])
    return myaddr