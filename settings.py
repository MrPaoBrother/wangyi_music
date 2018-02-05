# -*- coding:utf8 -*-

# 配置参数

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
    'Referer': 'http://music.163.com/'
}
page_offset = 0
page_limit = 20
first_param = "{rid:\"\", offset:\"%d\", total:\"true\", limit:\"%d\", csrf_token:\"\"}"
second_param = "010001"
third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
forth_param = "0CoJUm6Qyw8W8jud"

base_url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_%s/?csrf_token="

# 这里提供数据库配置
database_params = {
    "host": '',
    "port": '',
    "user": '',
    "password": '',
    "db": ''
}

# 下面是一些sql语句

