# -*- coding:utf-8 -*-
# @Time   : 2022-08-29
# @Author : link

import os
import sys
Flag = True
suffix = 0


def AllModify():
    os.chdir(path)  # 改变当前工作目录到指定的路径
    files = os.listdir(path)
    for fileSuffix in files:
        portion = os.path.splitext(fileSuffix)  # 分离文件名与后缀名，并放在一个列表中
        newName = portion[0] + "." + suffix
        os.rename(fileSuffix, newName)


def PartModify():
    os.chdir(path)
    files = os.listdir(path)
    for fileSuffix in files:
        portion = os.path.splitext(fileSuffix)  # 分离文件名与后缀名，并放在一个列表中
        if portion[1] == suffixBefore:
            newName = portion[0] + "." + suffixAfter
            os.rename(fileSuffix, newName)


while Flag:
    print("---本程序请直接右上角关闭 或 全部修改完之后输入3关闭---\n\n")
    path = input(r"请输入完整的文件夹路径(文件管理-右键路径-复制):")
    control = input("修改所有文件的后缀按1，修改指定后缀文件的后缀按2，关闭按3:\n\n")
    if control == "1":
        suffix = input("请输入修改后的文件后缀名[后缀不用加. 快捷键直接输数字]（快捷输入： 1/png 2/mp4 3/zip 4/exe 5/mp3）:\n\n")
        if suffix == "1":
            suffix = "png"
            AllModify()
            print("修改完成                                                     ")
        elif suffix == "2":
            suffix = "mp4"
            AllModify()
            print("修改完成                                                     ")
        elif suffix == "3":
            suffix = "zip"
            AllModify()
            print("修改完成                                                     ")
        elif suffix == "4":
            suffix = "exe"
            AllModify()
            print("修改完成                                                     ")
        elif suffix == "5":
            suffix = "mp3"
            AllModify()
            print("修改完成                                                     ")
        else:
            AllModify()
            print("修改完成                                                     ")
    elif control == "2":
        suffixBefore = "." + input("请输入修改前的文件后缀名:\n\n")
        suffixAfter = input("请输入修改后的文件后缀名[后缀不用加. 快捷键直接输数字]（快捷输入： 1/png 2/mp4 3/zip 4/exe 5/mp3）:\n\n")
        if suffixAfter == "1":
            suffixAfter = "png"
            PartModify()
            print("修改完成                                                     ")
        elif suffixAfter == "2":
            suffixAfter = "mp4"
            PartModify()
            print("修改完成                                                     ")
        elif suffixAfter == "3":
            suffixAfter = "zip"
            PartModify()
            print("修改完成                                                     ")
        elif suffixAfter == "4":
            suffixAfter = "exe"
            PartModify()
            print("修改完成                                                     ")
        elif suffixAfter == "5":
            suffixAfter = "mp3"
            PartModify()
            print("修改完成                                                     ")
        else:
            PartModify()
            print("修改完成                                                     ")
    elif control == "3":
        sys.exit()
    else:
        print("非法字符，请重新输入（请输入键盘上的1或者2）\n\n")
        Flag = True
