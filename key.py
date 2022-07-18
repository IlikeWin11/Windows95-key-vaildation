#! /usr/bin/python
# coding:UTF-8
import random
import sys
import os

if os.name == "nt":                                                                                        # 判断清屏命令
    cls = "cls"                                                                                            # Windows下cls清屏
else:
    cls = "clear"                                                                                          # Linux下clear清屏

def rule():                                                                                                # 查看 Windows 95/NT 4.0/Office 95序列号验证规则
    print("零售版密钥：\n")
    print("XXX-XXXXXXX")
    print("前3位数不能为333、444、555、666、777、888、999，后7位数各位数字相加之和必须为7的倍数。")
    asdf = input("请按任意键继续...")
    os.system(cls)
    main()

def mod7_check(number): 
    """
    作用：检查后7位数\r\n
    number:数字
    """
    number = str(int(number))
    a = 0                                                                                                 # 初始化总和为0
    for i in number:                                                                                      # 遍历字符串中的每一个数字                         
        a += int(i)                                                                                       # 累加数字
    if a % 7 == 0:                                                                                        # 判断总和是否为7的倍数
        return 1
    else:
        return 0

def check3(number):                                                                                      # 检查前3位数是否出现在黑名单中
    """
    作用：检查前3位数\r\n
    number:数字
    """
    number = str(number)
    if number == "333":
        return 0
    elif number == "444":
        return 0
    elif number == "555":
        return 0
    elif number == "666":
        return 0
    elif number == "777":
        return 0
    elif number == "888":
        return 0
    elif number == "999":
        return 0
    else:
        return 1

def check(key):
    """
    密钥检查流程。\r\n
    key:需要检查的密钥，以字符串（str）形式提交参数。
    """
    key = str(key)
    key_list = key.split("-")
    try:
        if check3(key_list[0]) == 1 and mod7_check(key_list[1]) == 1:
            print("有效密钥。")
            asdf = input("按任意键继续...")
            os.system(cls)
            main()
        else:
            print("无效密钥。")
            asdf = input("按任意键继续...")
            os.system(cls)
            main()
        asdf = input("按任意键继续...")
    except:
        os.system(cls)
        main()

def gen(number = 1):
    """
    生成序列号。
    number:序列号的个数，默认为1，可选参数。
    """
    for i in range(number):                                                                             # 用for循环重复执行命令
        a = random.randint(100,998)                                                                     # 生成一个随机数
        if number == "333":                                                                             # 检查生成的数是否出现在黑名单中，有则重来，没有则继续
            gen()
        elif number == "444":
            gen()
        elif number == "555":
            gen()
        elif number == "666":
            gen()
        elif number == "777":
            gen()
        elif number == "888":
            gen()
        elif number == "999":
            gen()
        else:
            b = random.randint(1000006, 9999999)
            c = 0
            for i in str(b):                                                                            # mod7_check检查
                c += int(i)
            if c % 7 == 0:
                print(str(a)+"-"+str(b))
                akdh = input("请按任意键继续...")
            else:
                gen()


def main():
    """主界面"""
    print("Windows 95 Product Key Checker")
    print("=" * 33 + "\n")
    print("1.查看验证机制\n2.验证序列号\n3.生成序列号")
    try:
        p = int(input("选项："))
    except:
        os.system(cls)
        main()
        
    if p == 1:
        os.system(cls)
        rule()
    elif p == 2:
        os.system(cls)
        check(str(input("密钥：")))
    elif p == 3:
        os.system(cls)
        gen(int(input("要生成多少个序列号？")))
    else:
        os.system(cls)
        main()

if __name__ == "__main__":
    """判断是否在主解析器中执行"""
    try:
        main()
    except:
        print("错误。")
        shdi = input("请按任意键继续...")
        os.system(cls)
        main()
