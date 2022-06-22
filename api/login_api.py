# -*- coding: utf-8 -*-
# @Time     : 2022-06-16 22:01
# Author    : yejq
from api.etf_api import EtfApi
from utils.logger import logger


class Login(EtfApi):
    def login_token(self):
        url = self.BASE_URL + "/g/bizframe/v/submitLogin"
        method = "POST"
        payload = {
            "operator_code": 99991000,
            "password": 0
        }
        r = self.etf_requests(url=url, method=method, data = payload)
        logger.debug(f"登录成功，返回信息为：{r.text}")
        return r

    def logout(self):
        pass