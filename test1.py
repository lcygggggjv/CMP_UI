


# class bas:
#
#
#     @staticmethod
#     def a():
#
#         print("这是实例方法")


# print(bas.a)

# def hello():
#
#     print("这是")
#
#
# def hc(function):
#
#     function()
#
# hc(hello)


import asyncio

import easyocr

from Config.file_path import FilePath


# def test_ts(list1: int):
#     print(f"{list1}")
#
# test_ts('23')

def easy_ocr():
    reader = easyocr.Reader(['en'])
    res = reader.readtext(FilePath.captcha_dir)
    for detection in res:
        print(detection[1])
        return detection[1]


sd = easy_ocr()
print(sd)
