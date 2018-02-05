# -*- coding:utf-8 -*-
"""
author: power
pub_time: 2018/02/05
"""

from code import *
from settings import *
from data_process import *


if __name__ == "__main__":
    # 音乐的id
    music_id = "436514312"
    url = base_url % music_id
    # 得到第一页到第五页的评论内容
    msg = get_comments(url, from_page=1, to_page=5)
    # 下面就是输出用户名和用户评论内容的例子
    example_print_user_and_content(msg)
