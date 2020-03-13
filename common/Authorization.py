#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
hearder里面的Authorization，用于鉴权
Bearer为
"""
from time import time
import jwt

def get_Author():
    localtime = int(time())
    life = localtime + 600
    playload={
        'user': {
            'uid': 4273916,
            'acId': 30855117380005888,
            'name': 'epet',
            'orgId': 100

        },
        'iat': localtime,
        'exp': life
       }
    header = {
        'typ': 'JWT',
        'alg': 'HS256' # 所使用的加密算法方式

    }
    #
    # s=authlib.
    jwt_token = jwt.encode(playload,  # payload, 有效载体
                           "dh324y5sd854asd4",  # 进行加密签名的密钥.线上：gtiudkli4845aert，测服：dh324y5sd854asd4
                           algorithm="HS256",  # 指明签名算法方式, 默认也是HS256
                           headers=header  # json web token 数据结构包含两部分, payload(有效载体), headers(标头)
                           ).decode('utf-8')  # python3 编码后得到 bytes, 再进行解码(指明解码的格式), 得到一个str

    # print('Bearer '+jwt_token)
    return jwt_token

author=get_Author()

