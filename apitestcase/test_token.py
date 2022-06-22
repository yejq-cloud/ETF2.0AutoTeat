# -*- coding: utf-8 -*-
# @Time     : 2022-06-13 22:00
# Author    : yejq
from api.etf_api import EtfApi


class TestToken(EtfApi):

    def test_token(self):
        etf_api = EtfApi()
        etf_api.get_token()
