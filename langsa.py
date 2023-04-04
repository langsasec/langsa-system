# -*- coding: UTF-8 -*-
# @Time:  11:45
# @Author: 浪飒
# @File: langsa.py
# @Software: PyCharm
import binascii

en_langsa = {
    '0': '00',
    '1': 'la',
    '2': 'ln',
    '3': 'lg',
    '4': 'ls',
    '5': 'l2',
    '6': 'an',
    '7': 'ag',
    '8': 'as',
    '9': 'aa',
    'a': 'ng',
    'b': 'ns',
    'c': 'na',
    'd': 'gs',
    'e': 'ga',
    'f': 'sa'
}

de_langsa = {
    '00': '0',
    'la': '1',
    'ln': '2',
    'lg': '3',
    'ls': '4',
    'l2': '5',
    'an': '6',
    'ag': '7',
    'as': '8',
    'aa': '9',
    'ng': 'a',
    'ns': 'b',
    'na': 'c',
    'gs': 'd',
    'ga': 'e',
    'sa': 'f'
}


# langsa进制编码
def encode_langsa(text):
    encode_text = ''
    # 转16进制
    text16 = text.encode("utf-8").hex()
    for i in text16:
        encode_text += en_langsa[i]
    return encode_text


def decode_langsa(text):
    text16 = ''
    for i in range(0,len(text),2):
        text16 = text16 + de_langsa[text[i:i + 2]]
    decode_text = binascii.a2b_hex(text16).decode()
    return decode_text

