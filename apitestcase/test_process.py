# -*- coding: utf-8 -*-
# @Time     : 2022-06-11 23:06
# Author    : yejq
import allure
from api.process_api import Process

@allure.feature("PCF流程模块")
class TestProcess:
    def setup_class(self):
        self.process = Process()

    def teardown_class(self):
        pass


    @allure.story("新增流程模板")
    def test_add_process(self):
        #新增流程模板，获取模板，断言模板是否创建成功
        r = self.process.add_process()
        print(r.json())
        #1.通过别的业务接口完成断言；2.封装一些数据库操作，读取数据库完成数据库断言。
        assert r.json().get("data")[0].get("error_no") == 0

    @allure.story("修改流程步骤")
    def test_modify_process(self):
        r = self.process.modify_process()
        assert r.json().get("data")[0].get("error_no") == 0

    @allure.story("查询流程步骤")
    def test_processquery(self):
        r = self.process.processquery()
        assert r.json().get('data')[0].get('error_no') == 0

    @allure.story("修改流程模板")
    def test_tmpl_modify(self):
        pass

    @allure.story("查询流程模板")
    def test_tmpl_query(self):
        r = self.process.tmpl_query()
        # print(r.json().get("data")[0].get('error_no'))
        assert r.json().get("data")[0].get('error_no') == 0

    @allure.story("删除流程模板")
    def test_tmpl_del(self):
        r = self.process.tmpl_del()
        assert r.json().get("data")[0].get("error_no") ==0