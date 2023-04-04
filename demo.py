# -*- coding: UTF-8 -*-
# @Time:  18:10
# @Author: 浪飒
# @File: demo.py
# @Software: PyCharm
from langsa import encode_langsa,decode_langsa
from 浪飒 import encode_Langsa,decode_Langsa


print(encode_langsa("langsasec"))
print(decode_langsa(encode_langsa("langsasec")))
print(encode_Langsa("langsasec"))
print(decode_Langsa(encode_Langsa("langsasec")))

