# -*- coding:utf8 -*-

from Crypto.Cipher import AES
import base64
import requests
from settings import *


def get_params():
    iv = "0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    h_encText = AES_encrypt(first_param % (page_offset, page_limit), first_key, iv)
    h_encText = AES_encrypt(h_encText, second_key, iv)
    return h_encText


def get_params_by_page(page_param):
    iv = "0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    h_encText = AES_encrypt(page_param, first_key, iv)
    h_encText = AES_encrypt(h_encText, second_key, iv)
    return h_encText


def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey


def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text


def get_json(url, params, encSecKey):
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    response = requests.post(url, headers=headers, data=data)
    return response.content


def get_json_by_url(url):
    data = {
        "params": get_params(),
        "encSecKey": get_encSecKey()
    }
    response = requests.post(url, headers=headers, data=data)
    return response.content


def get_comments(url, from_page=1, to_page=10):
    """
    按照分页得到评论
    :param url: 歌曲评论api
    :param from_page: 从第几页开始 默认0
    :param to_page: 到第几页 默认10
    :return:
    """
    result = []
    for i in range(from_page - 1, to_page):
        offset = i * page_limit
        limit = page_limit
        page_param = first_param % (offset, limit)
        params = get_params_by_page(page_param)
        encSecKey = get_encSecKey()
        json_text = get_json(url, params, encSecKey)
        result.append(json_text)
    return result

