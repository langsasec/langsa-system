# -*- coding: UTF-8 -*-
# @Time:  11:46
# @Author: 浪飒
# @File: 浪飒.py
# @Software: PyCharm


import binascii

en_Langsa = {
    '0': '浪浪浪浪',
    '1': '浪浪浪飒',
    '2': '浪浪飒浪',
    '3': '浪浪飒飒',
    '4': '浪飒浪浪',
    '5': '浪飒浪飒',
    '6': '浪飒飒浪',
    '7': '浪飒飒飒',
    '8': '飒浪浪浪',
    '9': '飒浪浪飒',
    'a': '飒浪飒浪',
    'b': '飒浪飒飒',
    'c': '飒飒浪浪',
    'd': '飒飒浪飒',
    'e': '飒飒飒浪',
    'f': '飒飒飒飒'
}
de_Langsa = {
    '浪浪浪浪': '0',
    '浪浪浪飒': '1',
    '浪浪飒浪': '2',
    '浪浪飒飒': '3',
    '浪飒浪浪': '4',
    '浪飒浪飒': '5',
    '浪飒飒浪': '6',
    '浪飒飒飒': '7',
    '飒浪浪浪': '8',
    '飒浪浪飒': '9',
    '飒浪飒浪': 'a',
    '飒浪飒飒': 'b',
    '飒飒浪浪': 'c',
    '飒飒浪飒': 'd',
    '飒飒飒浪': 'e',
    '飒飒飒飒': 'f'
}


# 浪飒进制编码
def encode_Langsa(text):
    # 将字符串转换为16进制（字符串可含汉字）
    text16 = text.encode("utf-8").hex()
    for i in en_Langsa:
        text16 = text16.replace(i, en_Langsa[i])
    encode_text = text16
    return encode_text


# 浪飒进制解码
def decode_Langsa(text):
    text16=''
    for i in range(0, len(text), 4):
        text16 = text16 + de_Langsa[text[i:i + 4]]
    decode_text = binascii.a2b_hex(text16).decode()
    return decode_text



