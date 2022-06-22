# -*- coding: utf-8 -*-
# @Time     : 2022-06-11 22:43
# Author    : yejq
import requests
from utils.logger import logger

class BaseApi:
    def base_requests(self, method, url, **kwargs):
        '''
        接口相关操作的封装，不涉及具体业务，方便更多系统或业务的调用。
        :param method: 请求方法
        :param url: 请求url
        :param kwargs: 参数
        :return: 返回请求供后续接口调用
        '''
        logger.debug(f"请求的methon是{method},请求的url是{url}")
        r = requests.request(method, url, **kwargs)
        return r


