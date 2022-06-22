# -*- coding: utf-8 -*-
# @Time     : 2022-06-16 22:05
# Author    : yejq
from api.login_api import Login


class Testlogin():
    def setup_class(self):
        self.login_token = Login()

    def test_login_token(self):
        self.login_token.login_token()

    def test_logout(self):
        pass

