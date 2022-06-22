# -*- coding: utf-8 -*-
# @Time     : 2022-06-11 22:48
# Author    : yejq
from re import split

from api.base_api import BaseApi
from configs.config import HOST_IP
from utils.logger import logger

'''
接口的具体实现内容：业务接口的相关操作method,url,kawargs
'''
class EtfApi(BaseApi):
    BASE_URL = HOST_IP #----基础url提取出来
    def __init__(self):
        '''
        初始化获取token，执行用例时每次只需要调用一次
        '''
        self.token = self.get_token()

    def etf_requests(self, url, method, **kwargs):
        '''
        etf系统业务接口操作方法封装，请求时需要加上登录返回的token
        :param url:
        :param method:
        :param kwargs:
        :return:
        '''
        if "headers" in kwargs:
            kwargs["headers"]["cookie"] = f"{self.token}"
            logger.debug(f'{kwargs["headers"]["cookie"]}')
        else:
            kwargs["headers"] = {"cookie":f"{self.token}"}
            logger.debug(f'kwargs["headers"]')
        r = self.base_requests(url=url, method=method, **kwargs)
        return r

    def get_token(self):
        '''
        获取token方法
        :return:
        '''
        url = self.BASE_URL + "/g/bizframe/v/submitLogin"
        method = "POST"
        payload = {
            "operator_code": 99991000,
            "password": 0
        }
        r = self.base_requests(url=url, method=method, data = payload)
        self.token = r.headers["Set-Cookie"].split(';')[0]
        # logger.debug(f"登录返回的头信息为：{r.headers}")
        logger.debug(f"登录返回的token信息为：{self.token}")
        return  self.token


    def send(self, url, method, **kwargs):
        '''
        封装发送请求方法send()
        :param url:
        :param method:
        :param kwargs:
        :return:
        '''
        url = self.BASE_URL + url
        return self.etf_requests(url=url, method=method, **kwargs)

